import datetime

from django.db import models
#from django.core.exceptions import ValidationError, ObjectDoesNotExist

from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.fields import ImageField

from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField

from ..base import models as kk


class ArticleAnnotationMixin(models.Model):
    annotation = models.TextField(
        'Аннотация',
        help_text = 'Заполните аннотацию и в списке статей<br />\
            будет показан этот текст, вместо основного текста статьи',
        blank = True
    )

    class Meta:
        abstract = True


class ArticleCoverMixin(models.Model):
    cover = models.ImageField(
        'Обложка',
        upload_to = 'images',
        blank = True
    )

    class Meta:
        abstract = True


#class EventTimeMixin(models.Model):
#    event_start = models.DateTimeField(
#        verbose_name = 'Время начала события',
#        help_text = 'Заполните, если в статье упомянуто событие\
#            (акция, фильм и т. д.)',
#        blank = True,
#        null = True,
#    )
#
#    event_end = models.DateTimeField(
#        verbose_name = 'Время завершения события',
#        help_text = 'Заполните, если время завершения события известно',
#        blank = True,
#        null = True,
#    )
#
#    class Meta:
#        abstract = True


class Article(kk.Base):
    fixed = models.BooleanField(
        verbose_name = 'Закреплена',
        help_text = 'Выводится в начале списка статей',
        default = False,
    )

    headline = models.CharField(
        'Заголовок',
        max_length = 255,
#        help_text="Текст: <em>Текст</em>."
    )

    content = RichTextUploadingField(
        'Содержимое',
        blank = True
    )

    pub_date = models.DateTimeField(
        'Время публикации',
        default = datetime.datetime.now
    )

    def __str__(self):
        return self.headline

    class Meta:
        abstract = True
        ordering = ('-fixed', '-pub_date', )
        verbose_name = 'статья'
        verbose_name_plural = 'Статьи'
