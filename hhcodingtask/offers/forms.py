from django import forms

from offers.models import Offer
from schemes.forms import BaseSchemeFormMixin


class OfferForm(BaseSchemeFormMixin, forms.ModelForm):

    class Meta:
        model = Offer
        exclude = ('id', 'created_at', 'updated_at', 'data')

    def __init__(self, *args, **kwargs):
        super(BaseSchemeFormMixin, self).__init__(*args, **kwargs)
        super(OfferForm, self).__init__(*args, **kwargs)
        self.init_scheme_fields()
