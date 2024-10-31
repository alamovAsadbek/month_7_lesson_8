from django.urls import path

from app_debts.views import *
from app_users.views import *

urlpatterns = [
    path('login/', login_user_view, name='login_user_view'),
    path('register/', register_user_view, name='register_user_view'),
    path('users/', get_user_view, name='get_user_view'),
    path('users/<int:user_id>/', get_user_by_id_view, name='get_user_by_id_view'),
    path('debts/', debts_view, name='debts_view')
]
