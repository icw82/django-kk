from django.urls import path
from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [
    path('files/',
        FileListView.as_api()),
    path('files/<int:id>/',
        FileView.as_api()),
]
