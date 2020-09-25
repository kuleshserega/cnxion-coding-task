from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


django_form_fields = {
    'String': forms.CharField(required=True),
    'Integer': forms.IntegerField(required=True),
    'Float': forms.FloatField(required=True,
                              validators=[MinValueValidator(0.0),
                                          MaxValueValidator(10000.0)]),
    'Boolean': forms.BooleanField(required=False),
}


class BaseSchemeFormMixin:

    def __init__(self, *args, **kwargs):
        self.object_id = kwargs.get('initial', {}).get('object_id')

    def init_scheme_fields(self):
        fields = [
            attr for attr in self.instance.scheme.__dict__
            if not callable(attr) and not attr.startswith('__')
        ]

        for field in fields:
            field_type = getattr(self.instance.scheme, field)
            self.fields[field] = django_form_fields.get(field_type)

    def save(self, *args, **kwargs):
        data = {}
        for field, value in self.cleaned_data.items():
            data[field] = value

        object_class = self.instance.__class__

        if not self.object_id:
            object_instance = object_class.objects.create(data=data)
            object_instance.save()
        else:
            object_class.objects.filter(pk=self.object_id).update(data=data)
