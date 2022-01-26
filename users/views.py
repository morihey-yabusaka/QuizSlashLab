from urllib.parse import *

from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.views import LoginView, LogoutView, SuccessURLAllowedHostsMixin, PasswordChangeView, PasswordChangeDoneView

from .models import User
from .forms import SignupForm, LoginForm

REDIRECT_QUERY_NAME = 'next'


class DynamicRedirectMixin(SuccessURLAllowedHostsMixin):
  """
  参考:
  [Django] フォームでログイン認証の時と同じようにnext=URLが使えるようにする | エンジニアもどきの技術メモ
  https://e-tec-memo.herokuapp.com/article/169/
  """
  redirect_query_name = REDIRECT_QUERY_NAME

  def get_success_url(self):
    return self.get_redirect_url() or super().get_success_url()

  def get_redirect_url(self):
    redirect_to = self.request.POST.get(
      self.redirect_query_name,
      self.request.GET.get(self.redirect_query_name, '')
    )
    url_is_safe = url_has_allowed_host_and_scheme(
      url=redirect_to,
      allowed_hosts=self.get_success_url_allowed_hosts(),
      require_https=self.request.is_secure(),
    )
    return redirect_to if url_is_safe else ''


class SignupView(DynamicRedirectMixin, CreateView):
  model = User
  template_name = 'signup.html'
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


class LogInView(LoginView):
  template_name = "login.html"
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
  template_name = "logout.html"

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


class PassWordChangeView(LoginRequiredMixin, PasswordChangeView):
  success_url = reverse_lazy('users:password_change_done')
  template_name = 'password_change.html'

password_change_view = PassWordChangeView.as_view()


class PassWordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
  template_name = 'password_change_done.html'

password_change_done_view = PassWordChangeDoneView.as_view()