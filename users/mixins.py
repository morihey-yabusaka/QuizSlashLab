from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.contrib.auth.mixins import UserPassesTestMixin

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


class OnlyMeMixin(UserPassesTestMixin):
  """
  Userの詳細を確認，編集する際に使用．
  ユーザ自身とスーパーユーザのみ閲覧可．
  参考:
  https://docs.djangoproject.com/ja/4.0/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
  """

  def test_func(self):
    user = self.request.user
    return user.pk == self.get_object().pk or user.is_superuser