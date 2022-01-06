from django.urls import path

from .views import *

app_name = 'users'
urlpatterns = [
  path('sineup', signup_view, name='signup'),
  path('login', login_view, name='login'),
  path('logout', logout_view, name='logout')
]