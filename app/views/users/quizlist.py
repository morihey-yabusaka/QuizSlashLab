from django.views.generic import ListView

from ...models import Quiz
from users.models import User

class UserQuizListView(ListView):
  model = Quiz
  context_object_name = 'quizes'
  template_name = "quiz/list.html"

  def get_queryset(self, **kwargs):
    queryset = User.objects.get(username=self.kwargs.get('slug')).quiz.publish().order_by('-updated_at')
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['title'] = [
      {'text': self.kwargs.get('slug') + 'の', 's': False},
      {'text': '作', 's': True},
      {'text': '問', 's': False},
    ]

    return context

user_quiz_list_view = UserQuizListView.as_view()