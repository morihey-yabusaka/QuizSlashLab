from django.views.generic.edit import FormView


from ...models import Quiz
from users.models import User

class BetamonView(FormView):

  def post(self, request, *args, **kwargs):
    print(request)


betamon_view = BetamonView.as_view()
