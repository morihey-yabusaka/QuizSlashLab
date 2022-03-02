from django.views.generic import ListView

from ...models import Quiz


class BetaMonUserList(ListView):
  """
  UserがBetaMonしたQuizの一覧
  """

  context_object_name = 'users'
  template_name = 'users/list.html'

  def get_queryset(self, **kwargs):
    pk = self.kwargs.get('pk')
    quiz = Quiz.objects.get(pk=pk)
    return quiz.betamon.user()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['title'] = [
        {'text': 'ベタ問したユーザー', 's': False},
    ]

    return context


betamon_user_list = BetaMonUserList.as_view()
