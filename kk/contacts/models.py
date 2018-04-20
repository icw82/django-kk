from django.db import models
#from django.core.exceptions import ValidationError, ObjectDoesNotExist

from kk.base import models as kk

#class TYPES:
#    EMAIL = 'email'
#    TEL = 'tel'
#    WEBSITE = 'website'
#    VK = 'vk'
#    FB = 'fb'
#    OK = 'ok'
#    TWITTER = 'tw'
#    INSTAGRAM = 'instagram'
#
#    CHOICES = (
#        (EMAIL, 'Электронная почта'),
#        (TEL, 'Телефон'),
#        (WEBSITE, 'Сайт'),
#        (VK, 'VK'),
#        (FB, 'Фейсбук'),
#        (OK, 'Одноклассники'),
#        (TWITTER, 'Твиттер'),
#        (INSTAGRAM, 'Инстаграм'),
#    )

class ContactType(kk.CodenameMixin, kk.Base):
    name = models.CharField(
        'Название',
        max_length = 160
    )

#    url = models.CharField(
#        'Основной адрес',
#        max_length = 160
#    )

    def __str__(self):
        return '{name} ({codename})'.format(
            name = self.name,
            codename = self.codename,
        )

    class Meta:
        abstract = True
#        unique_together = ('type', 'is_main')
        verbose_name = 'тип контакта'
        verbose_name_plural = 'Типы контактов'


class Contact(kk.PositionMixin, kk.Base):
     # TODO: Основной уникальный по типу
    is_main = models.BooleanField(
        'Основной',
        help_text = 'Будет показан прежде остальных того же типа'
    )

#    type = models.ForeignKey(
#        ContactType,
#        on_delete = models.PROTECT,
#        verbose_name = 'Модель',
#        related_name = 'contacts',
#        related_query_name = 'contacts',
#    )

    value = models.CharField(
        'Значение',
        max_length = 160
    )

    def __str__(self):
        return '{type} → {value}'.format(
            type = self.type.name,
            value = self.value,
        )

    class Meta:
        abstract = True
#        unique_together = ('type', 'is_main')
        verbose_name = 'контакт'
        verbose_name_plural = 'Все контакты'
