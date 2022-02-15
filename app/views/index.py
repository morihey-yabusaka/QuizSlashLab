from django.views.generic import TemplateView

from ..models import Quiz


class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self):
    context = super().get_context_data()
    todays = Quiz.objects.filter(is_todays_question=True)
    if todays.exists():
      todays = todays[0]

    context['todays'] = todays

    return context

index_view = IndexView.as_view()