from django.urls import path

from .views import *

app_name = 'users'
urlpatterns = [
  path('signup', signup_view, name='signup'),
  path('login', login_view, name='login'),
  path('logout', logout_view, name='logout'),
  path('password/change', password_change_view, name='password_change'),
  path('password/change/done', password_change_done_view, name='password_change_done')
]