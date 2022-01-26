from django.views.generic import DetailView

from users.models import User


class UserPageView(DetailView):
  model = User
  template_name = 'users/userpage.html'
  slug_field = 'username'
  context_object_name = "user_"

user_page_view = UserPageView.as_view()