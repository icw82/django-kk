from django.urls import path
from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [
    path('files/',
        FileListView.as_api()),
    path('files/<int:id>/',
        FileView.as_api()),

    path('files/information-disclosure/',
        InformationDisclosureFileListView.as_api()),
    path('files/information-disclosure/<int:id>/',
        InformationDisclosureFileView.as_api()),

    path('files/for-tenants/',
        ForTenantsFileListView.as_api()),
    path('files/for-tenants/<int:id>/',
        ForTenantsFileView.as_api()),
]
