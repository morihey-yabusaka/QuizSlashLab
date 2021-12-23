from django.urls import reverse
from django.views.generic import CreateView

from ...models import Quiz


class QuizCreateView(CreateView):
  model = Quiz
  template_name = '../templates/quiz/create.html'
  fields = ['question', 'answer', 'answer_yomi', 'author']

  def get_success_url(self):
      return reverse('quiz_detail', kwargs={'pk': self.object.pk})

quiz_create_view = QuizCreateView.as_view()