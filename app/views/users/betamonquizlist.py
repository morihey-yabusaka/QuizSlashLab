from django.views.generic import ListView

from ...models import BetaMon
from users.models import User


class BetaMonQuizList(ListView):
  """
  UserがBetaMonしたQuizの一覧
  """

  context_object_name = 'quizes'
  template_name='quiz/list.html'

  def get_queryset(self, **kwargs):
    username = self.kwargs.get('slug')
    user = User.objects.get(username=username)
    return user.betamon.quiz()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['title'] = [
      {'text': self.kwargs.get('slug') + 'の', 's': False},
      {'text': 'ベ', 's': True},
      {'text': 'タ問', 's': False},
    ]

    return context


betamon_quiz_list = BetaMonQuizList.as_view()