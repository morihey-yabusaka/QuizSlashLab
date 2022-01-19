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

user_quiz_list_view = UserQuizListView.as_view()