from django.views.generic import ListView

from ...models import GoodQuiz
from users.models import User


class GoodQuizQuizList(ListView):
  """
  UserがGoodQuizしたQuizの一覧
  """

  context_object_name = 'quizes'
  template_name='quiz/list.html'

  def get_queryset(self, **kwargs):
    username = self.kwargs.get('slug')
    user = User.objects.get(username=username)
    return user.good_quiz.quiz()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['title'] = [
      {'text': self.kwargs.get('slug') + 'の', 's': False},
      {'text': 'G', 's': True},
      {'text': 'oodQuiz', 's': False},
    ]

    return context


good_quiz_quiz_list = GoodQuizQuizList.as_view()