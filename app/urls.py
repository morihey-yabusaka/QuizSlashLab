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
  path('GoodQuiz/<int:quiz_pk>/<slug:slug>', good_quiz_view, name='good_quiz'), # gqの処理のみ
  path('BetaMon/<int:quiz_pk>/<slug:slug>', betamon_view, name='betamon'), # betamonの処理のみ
  path('user/draft/list', draft_list_view, name='draft_list'),
  path('<slug:slug>/quiz/list', user_quiz_list_view, name='user_quiz_list'),
  path('<slug:slug>/GoodQuiz/quiz', good_quiz_quiz_list, name='good_quiz_quiz_list'),
  path('<slug:slug>/BetaMon/quiz',
       betamon_quiz_list, name='betamon_quiz_list'),
  path('<int:pk>/GoodQuiz/user',
       good_quiz_user_list, name='good_quiz_user_list'),
  path('<int:pk>/BetaMon/user',
       betamon_user_list, name='betamon_user_list'),
  path('user/userpage/<slug:slug>', user_page_view, name='userpage'),
]