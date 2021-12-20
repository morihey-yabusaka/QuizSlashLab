from django.urls import path

from .views import *

urlpatterns = [
  path('', index_view, name='index'),
  path('quiz/list', quiz_list_view, name='quiz_list')
]