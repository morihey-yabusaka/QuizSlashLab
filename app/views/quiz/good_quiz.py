from django.http import JsonResponse
from django.views.generic.edit import FormView


from ...models import Quiz, GoodQuiz
from users.models import User

class GoodQuizView(FormView):

  def post(self, request, *args, **kwargs):
    quiz = Quiz.objects.get(pk=self.kwargs.get('quiz_pk'))
    user = User.objects.get(username=self.kwargs.get('slug'))
    good_quiz = GoodQuiz.objects.filter(quiz=quiz, user=user)

    if good_quiz.exists():
      good_quiz.delete()
    else:
      GoodQuiz.objects.create(quiz=quiz, user=user)

    return JsonResponse({})


good_quiz_view = GoodQuizView.as_view()
