from django.urls import path

from .views import *

app_name = 'users'
urlpatterns = [
  path('signup', signup_view, name='signup'),
  path('login', login_view, name='login'),
  path('logout', logout_view, name='logout'),
  path('password/change', password_change_view, name='password_change'),
  path('password/reset', password_reset_view, name='password_reset'),
  path('password/reset/done', password_reset_done_view, name='password_reset_done'),
  path('password/reset/confirm/<uidb64>/<token>', password_reset_confirm_view, name='password_reset_comfirm'),
  path('password/reset/complete', password_reset_complete_view, name='password_reset_complete'),
]