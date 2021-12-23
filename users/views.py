from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .models import User

class UserCreateView(CreateView):
  model = User
  template_name = 'create.html'
  fields = ('username', 'password')

user_create_view = UserCreateView.as_view()


class LoginView(TemplateView):
  pass

login_view = LoginView.as_view()

class LogoutView:
  pass