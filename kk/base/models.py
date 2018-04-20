from django.db import models

class TimeStumpsMixin(models.Model):
    created_date = models.DateTimeField(
        auto_now_add = True
    )

    modified_date = models.DateTimeField(
        auto_now = True
    )

    class Meta:
        abstract = True


class StatusMixin(models.Model):
    status = models.BooleanField(
        'Опубликовано',
#        help_text = 'Только латинcкими буквами',
        default = True
    )

    class Meta:
        abstract = True


class PositionMixin(models.Model):
    position = models.PositiveSmallIntegerField(
        'Позиция',
        null = True,
        blank = True
    )

    def unordered(self):
        return self.position == None

    class Meta:
        abstract = True


class CodenameMixin(models.Model):
    codename = models.SlugField(
        'Кодовое имя',
        max_length = 50,
        unique = True,
        help_text = 'Только латинcкими буквами',
        blank = True
    )

    class Meta:
        abstract = True


class XMLCodeMixin(models.Model):
    xml = models.TextField(
        'Код',
        blank = True
    )

    class Meta:
        abstract = True


class Base(
    StatusMixin,
    TimeStumpsMixin,
    models.Model,
):
    class Meta:
        abstract = True
