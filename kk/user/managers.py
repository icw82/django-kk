from django.db import models
#from django.contrib.auth.models import User

class UserQueryset(models.query.QuerySet):

    def active(self, *args):
        return self.filter(
            is_active = True
        )

    def staff(self, *args):
        return self.filter(
            is_staff = True
        )

    def superusers(self, *args):
        return self.filter(
            is_superuser = True
        )

    def completed(self, *args):
        return self.filter(
            name__isnull = False,
            sex__isnull = False,
        )

class UserManager(models.Manager):

#    .select_related('profile')

    def get_queryset(self):
        return UserQueryset(
            self.model,
            using = self._db
        )
# FIXME: Много запросов к user_profile (для каждого юзера новый запрос)
#        ).prefetch_related('profile')
#        ).select_related('profile')

    def completed(self, *args):
        return self.get_queryset().completed(*args)
