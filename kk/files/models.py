from datetime import datetime

from django.db import models

from ..base.models import Ordered

class File(Ordered):
    file = models.FileField(
        verbose_name = 'Файл',
        upload_to = 'uploads/%Y/%m/'
    )

    name = models.CharField(
        verbose_name = 'Название',
        help_text = 'Если пусто, в качестве названия будет использовано имя файла',
        blank = True,
        max_length = 250,
    )

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.file.name

    class Meta:
        abstract = True
        ordering = ['-name']
        verbose_name = 'файл'
        verbose_name_plural = 'Все файлы'
