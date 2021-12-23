from django.urls import path

from .views import *

urlpatterns = [
  path('', index_view, name='index'),
  path('quiz/list', quiz_list_view, name='quiz_list'),
  path('quiz/update/<int:pk>', quiz_update_view, name='quiz_update'),
  path('quiz/detail/<int:pk>', quiz_detail_view, name='quiz_detail'),
  path('quiz/create', quiz_create_view, name='quiz_create')
]