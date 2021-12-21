from django.views.generic import DetailView


from ...models import Quiz

class QuizDetailView(DetailView):
  model = Quiz
  template_name = "../templates/quiz/detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    question = context['object'].question
    context['n_start_equals'] = []
    for i in range(len(question)):
      n = Quiz.objects.filter(question__istartswith=question[:i+1]).count()-1
      context['n_start_equals'].append(n)
    return context

quiz_detail_view = QuizDetailView.as_view()