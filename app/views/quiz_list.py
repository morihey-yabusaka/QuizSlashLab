from django.views.generic import ListView

from ..models import Quiz

class QuizListView(ListView):
    model = Quiz
    template_name = "quizlist.html"

quiz_list_view = QuizListView.as_view()