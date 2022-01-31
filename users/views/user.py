from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView


from ..models import User
from ..forms import UserUpdateForm
from ..mixins import OnlyMeMixin

class UserDetailView(OnlyMeMixin, LoginRequiredMixin, DetailView):
  """
  登録情報詳細確認ビュー
  ユーザーページとは別
  """
  model = User
  template_name = 'user/detail.html'
  slug_field = 'username'
  context_object_name = 'user_'

user_detail_view = UserDetailView.as_view()


class UserUpdateView(OnlyMeMixin, LoginRequiredMixin, UpdateView):
  model = User
  template_name = 'user/update.html'
  slug_field = 'username'
  context_object_name = 'user_'
  form_class = UserUpdateForm

  def get_success_url(self):
    return reverse('users:user_detail', kwargs={'slug': self.object.username})

user_update_view = UserUpdateView.as_view()
