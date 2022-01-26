from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ...models import Quiz
from ...forms import QuizForm

class QuizCreateView(LoginRequiredMixin, CreateView):
  model = Quiz
  form_class = QuizForm
  template_name = 'quiz/create.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    if 'draft' in self.request.POST:
      form.instance.is_draft = True

    return super().form_valid(form)

  def get_success_url(self):
      return reverse('app:quiz_detail', kwargs={'pk': self.object.pk})

quiz_create_view = QuizCreateView.as_view()