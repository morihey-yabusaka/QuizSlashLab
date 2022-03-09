from django.views.generic import ListView

from ...models import Quiz


class GoodQuizUserList(ListView):
  """
  UserがGoodQuizしたQuizの一覧
  """

  context_object_name = 'users'
  template_name = 'users/list.html'

  def get_queryset(self, **kwargs):
    pk = self.kwargs.get('pk')
    quiz = Quiz.objects.get(pk=pk)
    return quiz.good_quiz.user()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['title'] = [
        {'text': 'GQしたユーザー', 's': False},
    ]

    return context


good_quiz_user_list = GoodQuizUserList.as_view()
