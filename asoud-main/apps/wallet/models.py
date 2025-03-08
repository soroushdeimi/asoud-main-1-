from apps.base.models  import models, BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Wallet(BaseModel):
    user = models.OneToOneField(
        related_name='wallet',
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )

    balance = models.PositiveIntegerField(
        verbose_name=_('Balance')
    )