from django.urls import reverse
from django.views.generic import CreateView

from ...models import Quiz


class QuizCreateView(CreateView):
  model = Quiz
  template_name = 'quiz/create.html'
  fields = ['question', 'answer', 'answer_yomi']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def get_success_url(self):
      return reverse('app:quiz_detail', kwargs={'pk': self.object.pk})

quiz_create_view = QuizCreateView.as_view()