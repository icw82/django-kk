from django.db import models

from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.fields import ImageField

from ..base import models as kk
from ..places.models import Place


class LogoMixin(models.Model):
    logo = models.ImageField(
        verbose_name = 'Логотип',
        upload_to = 'images/logos',
        blank = True
    )

#    def thumb(self):
#        return get_thumbnail(self.image, '80x60', crop = 'center')

    class Meta:
        abstract = True


class Entity(kk.Base):

    name = models.CharField(
        verbose_name = 'Название',
        max_length = 120
    )

    open = models.BooleanField(
        verbose_name = 'Открыто',
        help_text = 'Снимите флажок, если организация не функционирует',
        default = True
    )


#    place = models.OneToOneField(
#        Place,
#        on_delete = models.PROTECT,
#        verbose_name = 'место нахождения',
#        related_name = 'entities',
#        related_query_name = 'entity',
#        blank = True,
#        null = True,
#        editable = False,
##        unique = True, # OneToOneField
#    )

    def __str__(self):
        return '{name} ({type})'.format(
            name = self.name,
            type = self.get_type_display(),
        )

    class Meta:
        abstract = True
        ordering = ('name', )
        verbose_name = 'Организация'
        verbose_name_plural = 'Все организации'
