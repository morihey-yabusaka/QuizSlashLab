from django.views.generic import ListView

from ...models import Quiz

class QuizListView(ListView):
    model = Quiz
    context_object_name = 'quizes'
    ordering = ['-created_at']
    template_name = "quiz/list.html"


quiz_list_view = QuizListView.as_view()