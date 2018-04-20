from django.contrib import admin

from kk.base.admin import BaseAdmin, OrderedAdmin

from .models import *

#class ChildsInline(admin.TabularInline):
#    model = Place
#    extra = 0
#    readonly_fields = (
#        'name',
#        'type',
#        'parent',
#        'status',
#    )
#    can_delete = False
#    ordering = ('name', )
#
#    def has_add_permission(self, request):
#        return False

class PlaceAdmin(BaseAdmin):
    fields = (
        'status',
        'name',
        'type',
        'parent',
    )

    readonly_fields = ('parent', 'type')

    list_display = (
        'name',
        'type',
        'parent',
        'status',
    )

#    inlines = (ChildsInline, )
