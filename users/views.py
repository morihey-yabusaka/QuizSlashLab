from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from .models import User

class SignupView(CreateView):
  model = User
  template_name = 'signup.html'
  fields = ('username', 'password')

  def get_success_url(self):
    pass

signup_view = SignupView.as_view()


class LogInView(LoginView):
  template_name = "login.html"

login_view = LogInView.as_view()

class LogOutView(LogoutView):
  template_name = "logout.html"

logout_view = LogOutView.as_view()