from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from apps.base.models import models, BaseModel
from apps.users.models import User
from apps.market.models import Market
from apps.comment.models import Comment

# Create your models here.


class ProductKeyword(BaseModel):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    class Meta:
        db_table = 'product_keyword'
        verbose_name = _('Product keyword')
        verbose_name_plural = _('Product keywords')

    def __str__(self):
        return self.name


class ProductTheme(BaseModel):
    market = models.ForeignKey(
        Market,
        on_delete=models.CASCADE,
        verbose_name=_('Market'),
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_('Order'),
    )

    class Meta:
        db_table = 'product_theme'
        verbose_name = _('Product theme')
        verbose_name_plural = _('Product themes')

    def __str__(self):
        return self.name


class Product(BaseModel):
    GOOD = "good"
    SERVICE = "service"

    TYPE_CHOICES = (
        (GOOD, _("Good")),
        (SERVICE, _("Service")),
    )

    MARKET = "market"
    CUSTOMER = "customer"
    FREE = "free"

    SHIP_COST_PAY_TYPE_CHOICES = (
        (MARKET, _("Market")),
        (CUSTOMER, _("Customer")),
        (FREE, _("Free")),
    )

    DRAFT = "draft"
    QUEUE = "queue"
    NOT_PUBLISHED = "not_published"
    PUBLISHED = "published"
    NEEDS_EDITING = "needs_editing"
    INACTIVE = "inactive"

    STATUS_CHOICES = (
        (DRAFT, _("Draft")),
        (QUEUE, _("In Queue for Publication")),
        (NOT_PUBLISHED, _("Not Published")),
        (PUBLISHED, _("Published")),
        (NEEDS_EDITING, _("Needs Editing")),
        (INACTIVE, _("Inactive")),
    )

    ONLINE = "online"
    PERSON = "person"
    BOTH = "both"

    SELL_TYPE_CHOICES = (
        (ONLINE, _("Online")),
        (PERSON, _("Person")),
        (BOTH, _("Both")),
    )

    NEW = "new"
    SPECIAL_OFFER = "special_offer"
    COMING_SOON = "coming_soon"
    NONE = "none"

    TAG_CHOICES = (
        (NEW, _("New")),
        (SPECIAL_OFFER, _("Special Offer")),
        (COMING_SOON, _("Coming Soon")),
        (NONE, _("None")),
    )

    TOP_LEFT = "top_left"
    TOP_RIGHT = "top_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT = "bottom_right"

    TAG_POSITION_CHOICES = (
        (TOP_LEFT, _("Top Left")),
        (TOP_RIGHT, _("Top Right")),
        (BOTTOM_LEFT, _("Bottom Left")),
        (BOTTOM_RIGHT, _("Bottom Right")),
    )

    market = models.ForeignKey(
        Market,
        on_delete=models.CASCADE,
        verbose_name=_('Market'),
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description'),
    )

    technical_detail = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Technical detail'),
    )

    keywords = models.ManyToManyField(
        ProductKeyword,
        related_name='products',
        blank=True,
        verbose_name=_('Keywords'),
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Stock'),
    )

    price = models.DecimalField(
        max_digits=14,
        decimal_places=3,
        verbose_name=_('Price'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=DRAFT,
        verbose_name=_('Status'),
    )

    required_product = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='dependent_products',
        help_text="Another product that is required for this product.",
        verbose_name=_('Required product'),
    )

    gift_product = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='gift_products',
        verbose_name=_('Gift product'),
    )

    is_marketer = models.BooleanField(
        default=False,
        verbose_name=_('Is marketer'),
    )

    marketer_price = models.DecimalField(
        max_digits=14,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name=_('Marketer price'),
    )

    tag = models.CharField(
        max_length=20,
        choices=TAG_CHOICES,
        default=NONE,
        verbose_name=_("Tag"),
    )

    tag_position = models.CharField(
        max_length=20,
        choices=TAG_POSITION_CHOICES,
        default=TOP_LEFT,
        verbose_name=_("Tag Position"),
    )

    sell_type = models.CharField(
        max_length=10,
        choices=SELL_TYPE_CHOICES,
        default=ONLINE,
        verbose_name=_('Sell type'),
    )

    ship_cost = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name=_('Ship cost'),
    )

    ship_cost_pay_type = models.CharField(
        max_length=10,
        choices=SHIP_COST_PAY_TYPE_CHOICES,
        verbose_name=_('Ship cost pay type')
    )

    comments = GenericRelation(
        Comment,
        related_query_name='market_comments',
    )

    theme = models.ForeignKey(
        ProductTheme,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='products',
        verbose_name=_('Theme')
    )

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )

    image = models.ImageField(
        upload_to='product/image/',
        verbose_name=_('Image'),
    )

    class Meta:
        db_table = 'product_image'
        verbose_name = _('Product image')
        verbose_name_plural = _('Product images')

    def __str__(self):
        return self.product.name
