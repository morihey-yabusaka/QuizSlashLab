from django.views.generic import DetailView


from ..models import Quiz

class QuizDetailView(DetailView):
  model = Quiz
  template_name = "../templates/quiz/detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

quiz_detail_view = QuizDetailView.as_view()