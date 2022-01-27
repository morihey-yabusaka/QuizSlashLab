from django.views.generic import DetailView, UpdateView, DeleteView

from ..models import User


class UserDetailView(DetailView):
  """
  登録情報詳細確認ビュー
  ユーザーページとは別
  """
