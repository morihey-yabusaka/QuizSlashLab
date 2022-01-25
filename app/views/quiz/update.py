from django.urls import reverse
from django.views.generic import UpdateView

from ...models import Quiz
from ...forms import QuizForm
from ...mixins import AuthorOnlyEditableMixin

class QuizUpdateView(AuthorOnlyEditableMixin, UpdateView):
  model = Quiz
  form_class = QuizForm
  template_name = 'quiz/update.html'

  def get_success_url(self):
      return reverse('app:quiz_detail', kwargs={'pk': self.object.pk})

quiz_update_view = QuizUpdateView.as_view()