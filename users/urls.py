from django.urls import path

from .views import *

urlpatterns = [
  path('create', user_create_view, name='users_create'),
  path('login', login_view, name='login')
]