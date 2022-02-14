from django.views.generic.edit import FormView


from ...models import Quiz
from ....users.models import User

class QoodQuizView(FormView):

  def post(self, request, *args, **kwargs):
    print(request)
