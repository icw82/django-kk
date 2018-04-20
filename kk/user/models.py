from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User as OriginalUser

from sorl.thumbnail.fields import ImageField
from sorl.thumbnail import get_thumbnail

from core.models import Base

from .managers import UserManager


class User(OriginalUser):
    objects = UserManager()

    class Meta:
        proxy = True

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )

    name = models.CharField(
        'Имя',
        max_length = 128,
        null = True,
        blank = False
    )

    @property
    def is_completed(self):
        if self.name != None:
            return False

        return True


#    is_completed = property(_is_completed)

#    def __init__(self):
#        self._x = None
#
#    @property
#    def x(self):
#        """I'm the 'x' property."""
#        return self._x
#
#    @x.setter
#    def x(self, value):
#        self._x = value
#
#    @x.deleter
#    def x(self):
#        del self._x

#    def thumb(self):
#        return get_thumbnail(self.image, '80x60', crop = 'center')

@receiver(models.signals.post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(models.signals.post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
