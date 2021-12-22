from django.views.generic import DetailView


from ...models import Quiz, Slash

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

    slashes = Slash.objects.filter(quiz=context['object'])
    slashes = list(slashes.values())
    context['slashes'] = []
    for slash in slashes:
      tmp = {}
      for k,v in slash.items():
        tmp[k] = v
      if slash['n_push'] != 0:
        correct_ratio = slash['n_correct'] / slash['n_push'] * 100
        correct_ratio = str(correct_ratio).split(".")[0] + "%"
      else:
        correct_ratio = "-"
      tmp['correct_ratio'] = correct_ratio
      context['slashes'].append(tmp)
    return context

quiz_detail_view = QuizDetailView.as_view()