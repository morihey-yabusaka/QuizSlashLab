from django.http import JsonResponse
from django.views.generic.edit import FormView


from ...models import Quiz, BetaMon
from users.models import User

class BetaMonView(FormView):

  def post(self, request, *args, **kwargs):
    quiz = Quiz.objects.get(pk=self.kwargs.get('quiz_pk'))
    user = User.objects.get(username=self.kwargs.get('slug'))
    betamon = BetaMon.objects.filter(quiz=quiz, user=user)

    if betamon.exists():
      betamon.delete()
    else:
      BetaMon.objects.create(quiz=quiz, user=user)

    return JsonResponse({})


betamon_view = BetaMonView.as_view()
