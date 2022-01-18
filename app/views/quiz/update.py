from django.urls import reverse
from django.views.generic import UpdateView

from ...models import Quiz
from ...mixins import AuthorOnlyEditableMixin

class QuizUpdateView(AuthorOnlyEditableMixin, UpdateView):
  model = Quiz
  template_name = 'quiz/update.html'
  fields = ['question', 'answer', 'answer_yomi']

  def get_success_url(self):
      return reverse('quiz_detail', kwargs={'pk': self.object.pk})

quiz_update_view = QuizUpdateView.as_view()