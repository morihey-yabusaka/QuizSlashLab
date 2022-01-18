from django.views.generic import DeleteView

from ...models import Quiz


class QuizDeleteView(DeleteView):
  model = Quiz
  template_name = "quiz/delete.html"

quiz_delete_view = QuizDeleteView.as_view()