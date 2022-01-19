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

draft_list_view = DraftListView.as_view()