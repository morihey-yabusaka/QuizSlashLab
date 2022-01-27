from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.views import SuccessURLAllowedHostsMixin

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