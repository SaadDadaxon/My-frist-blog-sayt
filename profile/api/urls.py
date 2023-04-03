from django.urls import path
from rest_framework.authtoken import views
from .views import MyProfile, ProfileList

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('my/profile/', MyProfile.as_view()),
    path('my/profile/list/', ProfileList.as_view()),
]
