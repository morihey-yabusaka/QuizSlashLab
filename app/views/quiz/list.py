from django.db.models import Q
from django.views.generic import ListView

from ...models import Quiz

class QuizListView(ListView):
    model = Quiz
    context_object_name = 'quizes'
    ordering = ['-created_at']
    template_name = "quiz/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        question_query = self.request.GET.get('question')
        answer_query = self.request.GET.get('answer')

        # question and answer
        queryset = queryset.filter(Q(question__icontains=question_query)) if question_query else queryset
        queryset = queryset.filter(Q(answer__icontains=answer_query)) if answer_query else queryset

        return queryset


quiz_list_view = QuizListView.as_view()