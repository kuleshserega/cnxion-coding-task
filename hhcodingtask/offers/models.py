from decimal import Decimal

from jsonfield import JSONField
from django.db import models

from config.settings.schemes import OfferSchemeFields


class AbstractSchemeModel(models.Model):
    scheme = None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data = JSONField(null=True)

    class Meta:
        abstract = True


class Offer(AbstractSchemeModel):
    scheme = OfferSchemeFields

    def __str__(self):
        return str(self.id)
