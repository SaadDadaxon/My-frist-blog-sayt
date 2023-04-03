from django.urls import path
from .views import AboutListCreateAPI


urlpatterns = [
    path('list-create/', AboutListCreateAPI.as_view())
]
