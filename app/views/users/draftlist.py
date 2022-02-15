from django.views.generic import ListView

from ...models import Quiz


class DraftListView(ListView):
  model = Quiz
  context_object_name = 'quizes'
  ordering = ['-created_at']
  template_name = "quiz/list.html"

  def get_queryset(self, **kwargs):
    queryset = super().get_queryset(**kwargs)
    queryset = queryset.filter(is_draft=True, author=self.request.user)
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['title'] = [
      {'text': self.request.user.username + 'の', 's': False},
      {'text': '下', 's': True},
      {'text': '書き', 's': False},
    ]

    return context

draft_list_view = DraftListView.as_view()