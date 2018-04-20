from django.db import models

from sorl import thumbnail
from sorl.thumbnail.fields import ImageField

from ..base.models import Base, OrderedMixin

from entities.models import *
from articles.models import *
#from . import commons

class Gallery(OrderedMixin, Base):

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'


class Slide(OrderedMixin, Base):
    original_image = thumbnail.fields.ImageField(
        verbose_name = 'изображение',
        upload_to = 'images/slides',
    )

    caption = models.CharField(
        verbose_name = 'Подпись к изображению',
        help_text = 'Не более 250 символов',
        max_length = 250,
        blank = True,
    )

    gallery = models.ForeignKey(
        Gallery,
        on_delete = models.CASCADE,
        verbose_name = 'галерея',
        related_name = 'slides',
        related_query_name = 'slide',
    )

    def delete(self):
        filters = super(Slide, self).delete()
        thumbnail.delete(self.original_image)

#    def __str__(self):
#        return self.name

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'слайды галереи'
