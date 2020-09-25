from django.db import models

from jsonfield import JSONField


class AbstractSchemeModel(models.Model):
    scheme = None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data = JSONField(null=True)

    class Meta:
        abstract = True
