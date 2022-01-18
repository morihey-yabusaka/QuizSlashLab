from django.urls import reverse_lazy
from django.views.generic import DeleteView

from ...models import Quiz
from ...mixins import AuthorOnlyEditableMixin


class QuizDeleteView(AuthorOnlyEditableMixin, DeleteView):
  model = Quiz
  template_name = "quiz/delete.html"

  def get_success_url(self):
    return reverse_lazy('app:quiz_list')

quiz_delete_view = QuizDeleteView.as_view()