from schemes.config import OfferSchemeFields
from schemes.models import AbstractSchemeModel


class Offer(AbstractSchemeModel):
    scheme = OfferSchemeFields

    def __str__(self):
        return str(self.id)
