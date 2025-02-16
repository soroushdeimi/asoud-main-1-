from django.utils.translation import gettext_lazy as _

from apps.base.models import models, BaseModel
from apps.users.models import User
from apps.product.models import Product

# Create your models here.


class Cart(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description'),
    )

    class Meta:
        db_table = 'cart'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return self.user.mobile_number

    def total_price(self):
        # TODO: Handle discount section
        return sum(item.total_price() for item in self.cartitem_set.all())

    def total_items(self):
        return sum(item.quantity for item in self.cartitem_set.all())


class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name=_('Cart'),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name=_('Quantity'),
    )

    class Meta:
        db_table = 'cart_item'
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart {self.cart.id}"

    def total_price(self):
        return self.product.price * self.quantity


class CartPayment(BaseModel):
    CASH = "cash"
    ONLINE = "online"
    TRANSFER = "transfer"
    CHECK = "check"

    TYPE_CHOICES = (
        (CASH, _("Cash")),
        (ONLINE, _("Online")),
        (TRANSFER, _("Transfer")),
        (CHECK, _("Check")),
    )

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

    STATUS_CHOICES = (
        (PENDING, _("Pending")),
        (COMPLETED, _("Completed")),
        (FAILED, _("Failed")),
    )

    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        verbose_name=_('Cart'),
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        verbose_name=_('Type'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
        verbose_name=_('Status'),
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Amount'),
    )

    class Meta:
        db_table = 'cart_payment'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __str__(self):
        return f"Payment {self.id} for Cart {self.cart.id}"
