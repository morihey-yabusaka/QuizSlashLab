from django.views.generic import ListView

from ...models import Quiz


class UserQuizListView(ListView):
  model = Quiz
  context_object_name = 'quizes'
  ordering = ['-created_at']
  template_name = "quiz/list.html"

  def get_queryset(self, **kwargs):
    queryset = super().get_queryset(**kwargs)
    queryset = queryset.filter(is_draft=False, author=self.request.user)
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['title'] = [
      {'text': self.request.user.username + 'の', 's': False},
      {'text': '作', 's': True},
      {'text': '問', 's': False},
    ]

    return context

user_quiz_list_view = UserQuizListView.as_view()