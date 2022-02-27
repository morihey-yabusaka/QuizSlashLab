from django.views.generic import DetailView

from users.models import User
from ...models import Quiz


class UserPageView(DetailView):
  model = User
  template_name = 'users/userpage.html'
  slug_field = 'username'
  context_object_name = "user_"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.get_object()
    updated = user.quiz.publish().order_by('-updated_at')[:5]
    context['updated'] = updated
    gq = user.good_quiz.quiz().publish()[:5]
    context['goodquiz'] = gq
    betamon = user.betamon.quiz().publish()[:5]
    context['betamon'] = betamon

    return context


user_page_view = UserPageView.as_view()