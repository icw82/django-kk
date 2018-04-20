from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from kk.base.models import Base

# !!! https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/

class Place(Base):

    name = models.CharField(
        'Название',
#        help_text = '<em>Например:</em> 12-е место',
        max_length = 60
    )

    parent = models.ForeignKey(
        'self',
        on_delete = models.PROTECT,
        verbose_name = 'место нахождения',
        related_name = 'childs',
        related_query_name = 'child',
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name = 'место'
        verbose_name_plural = 'Все места'
