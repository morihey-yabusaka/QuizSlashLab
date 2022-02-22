from django.urls import reverse
from django.views.generic import DetailView
from django.http import HttpResponseRedirect


from ...models import Quiz, Slash

class QuizDetailView(DetailView):
  model = Quiz
  template_name = "quiz/detail.html"

  def post(self, request, *args, **kwargs):
    obj = self.get_object()
    if 'draft' in request.POST:
      obj.is_draft = True
    elif 'publish' in request.POST:
      obj.is_draft = False

    obj.save()

    return HttpResponseRedirect(reverse('app:quiz_detail', kwargs={'pk': obj.pk}))


quiz_detail_view = QuizDetailView.as_view()