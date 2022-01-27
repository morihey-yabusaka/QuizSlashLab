from urllib.parse import *

from django.contrib.auth import login
from django.views.generic import CreateView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView

from ..models import User
from ..forms import SignupForm, LoginForm
from ..mixins import DynamicRedirectMixin


class LogInView(LoginView):
  template_name = "authentication/login.html"
  form_class = LoginForm

  def get_success_url(self) -> str:
    """
    ログイン成功時のリダイレクトurlにクエリを追加．
    state=loginに．

    参考:
    PythonでURLのクエリ文字列（パラメータ）を取得・作成・変更 | note.nkmk.me
    https://note.nkmk.me/python-urllib-parse-query-string/
    django/views.py at main · django/django
    https://github.com/django/django/blob/main/django/contrib/auth/views.py
    """
    url = super().get_success_url()
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    state = query_dict.get('state')
    if state:
      query_dict['state'].append("login")
    else:
      query_dict['state'] = 'login'

    return urlunparse(parsed_url._replace(query=urlencode(query_dict, doseq=True)))


login_view = LogInView.as_view()


class LogOutView(LogoutView):
  template_name = "authentication/logout.html"

  def get_next_page(self) -> str:
    """
    ログアウト時のリダイレクトurlにクエリを追加．
    state=logoutに．

    参考:
    PythonでURLのクエリ文字列（パラメータ）を取得・作成・変更 | note.nkmk.me
    https://note.nkmk.me/python-urllib-parse-query-string/
    django/views.py at main · django/django
    https://github.com/django/django/blob/main/django/contrib/auth/views.py
    """
    url = super().get_next_page()
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    state = query_dict.get('state')
    if state:
      query_dict['state'].append("logout")
    else:
      query_dict['state'] = 'logout'

    return urlunparse(parsed_url._replace(query=urlencode(query_dict, doseq=True)))

logout_view = LogOutView.as_view()


class SignupView(DynamicRedirectMixin, CreateView):
  model = User
  template_name = 'authentication/signup.html'
  success_url = '/'
  form_class = SignupForm

  def get_success_url(self) -> str:
    """
    ログイン成功時のリダイレクトurlにクエリを追加．
    state=loginに．

    参考:
    PythonでURLのクエリ文字列（パラメータ）を取得・作成・変更 | note.nkmk.me
    https://note.nkmk.me/python-urllib-parse-query-string/
    django/views.py at main · django/django
    https://github.com/django/django/blob/main/django/contrib/auth/views.py
    """
    url = super().get_success_url()
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    state = query_dict.get('state')
    if state:
      query_dict['state'].append("login")
    else:
      query_dict['state'] = 'login'

    return urlunparse(parsed_url._replace(query=urlencode(query_dict, doseq=True)))

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    self.object = user
    return HttpResponseRedirect(self.get_success_url())

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['next'] = self.request.POST.get(
      self.redirect_query_name,
      self.request.GET.get(self.redirect_query_name, '')
    )
    return context


signup_view = SignupView.as_view()