import json

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from offers.models import Offer

django_form_fields = {
    'String': forms.CharField(required=True),
    'Integer': forms.IntegerField(required=True),
    'Float': forms.FloatField(required=True,
                              validators=[MinValueValidator(0.0),
                                          MaxValueValidator(10000.0)]),
}


class BaseSchemeMixin:

    def init_scheme_fields(self):
        fields = [
            attr for attr in self.instance.scheme.__dict__
            if not callable(attr) and not attr.startswith('__')
        ]

        for field in fields:
            field_type = getattr(self.instance.scheme, field)
            self.fields[field] = django_form_fields.get(field_type)


class OfferForm(forms.ModelForm, BaseSchemeMixin):

    class Meta:
        model = Offer
        exclude = ('id', 'created_at', 'updated_at', 'data')

    def __init__(self, *args, **kwargs):
        self.offer_id = kwargs.get('initial', {}).get('offer_id')
        super(OfferForm, self).__init__(*args, **kwargs)
        self.init_scheme_fields()

    def save(self, *args, **kwargs):
        data = {}
        for field, value in self.cleaned_data.items():
            data[field] = value

        if not self.offer_id:
            offer = Offer.objects.create(data=data)
            offer.save()
        else:
            Offer.objects.filter(pk=self.offer_id).update(data=data)
