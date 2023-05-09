from rest_framework import routers
from .views import *
from django.urls import path, include

urlpatterns = [
    # path(r'users/', UserListView.as_view()),
    path(r'signup/', UserCreateView.as_view()),
    path(r'users/<str:pk>', UserRetrieveView.as_view()),
    path(r'users/<str:pk>', UserPatchView.as_view()),
    path(r'close/', UserDeleteView.as_view()),
]
