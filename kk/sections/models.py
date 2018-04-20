from django.db import models
from ..base import models as kk
from mptt.models import MPTTModel, TreeForeignKey

class Section(
    kk.StatusMixin,
    kk.TimeStumpsMixin,
    MPTTModel
):
    parent = TreeForeignKey(
        'self',
        verbose_name = 'Родительский раздел',
        on_delete = models.PROTECT,
        null = True,
        blank = True,
        related_name = 'children',
        db_index = True
    )

    slug = models.SlugField(
        verbose_name = 'Слаг',
        max_length = 50,
        help_text = 'Только латинcкими буквами'
    )

    name = models.CharField(
        verbose_name = 'Название',
        max_length = 140
    )

    name_in_nav = models.CharField(
        'Название для навигации',
        max_length = 80,
        blank = True
    )

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower();
        super().save(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.name, self.slug)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        abstract = True
        unique_together = ('parent', 'slug');
#        ordering = ['-name']
        verbose_name = 'раздел'
        verbose_name_plural = 'Разделы'
