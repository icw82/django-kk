from django.contrib import admin

from kk.base.admin import BaseAdmin

from .models import *

class FileAdmin(BaseAdmin):
    fields = (
        'status',
        'position',
        'name',
        'file',
    )

    list_display = (
        '__str__',
        'position',
        'status',
    )
