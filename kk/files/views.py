#from datetime import datetime

from kk.api.views import (BaseAPI, ResourceMixin, CollectionMixin)
from .models import *


class FileMixin(BaseAPI):
    model = File # ForTenantsFile

    exported_data = [
        'id',
        'position',
        'name',
        'file.url as file',
    ]

class FileView(FileMixin, ResourceMixin): pass
class FileListView(FileMixin, CollectionMixin): pass


class InformationDisclosureFileMixin(BaseAPI):
    model = InformationDisclosureFile # ForTenantsFile

    exported_data = [
        'id',
        'position',
        'pub_date',
        'name',
        'file.url as file',
    ]

class InformationDisclosureFileView(
    InformationDisclosureFileMixin, ResourceMixin): pass
class InformationDisclosureFileListView(
    InformationDisclosureFileMixin, CollectionMixin): pass


class ForTenantsFileMixin(BaseAPI):
    model = ForTenantsFile

    exported_data = [
        'id',
        'position',
        'pub_date',
        'name',
        'file.url as file',
    ]

class ForTenantsFileView(ForTenantsFileMixin, ResourceMixin): pass
class ForTenantsFileListView(ForTenantsFileMixin, CollectionMixin): pass
