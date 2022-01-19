from django.urls import path

from .views import *

app_name = 'app'
urlpatterns = [
  path('', index_view, name='index'),
  path('quiz/list', quiz_list_view, name='quiz_list'),
  path('quiz/create', quiz_create_view, name='quiz_create'),
  path('quiz/update/<int:pk>', quiz_update_view, name='quiz_update'),
  path('quiz/detail/<int:pk>', quiz_detail_view, name='quiz_detail'),
  path('quiz/delete/<int:pk>', quiz_delete_view, name='quiz_delete'),
  path('quiz/user/draft', draft_list_view, name='draft_list'),
  path('quiz/user/quiz/list', user_quiz_list_view, name='user_quiz_list'),
]