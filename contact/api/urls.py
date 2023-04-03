from django.urls import path
from .views import ContactListCreateAPI

urlpatterns = [
    path('contact-list-create/', ContactListCreateAPI.as_view())
]
