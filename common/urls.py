from django.urls import path

from app_users.views import *

urlpatterns = [
    path('', login_user_view, name='login_user_view'),
    path('register/', register_user_view, name='register_user_view'),
]
