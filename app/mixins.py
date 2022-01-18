from django.contrib.auth.mixins import UserPassesTestMixin


class AuthorOnlyEditableMixin(UserPassesTestMixin):
  """
  データをその作成者のみ編集可能にする．
  UpdateView, DeleteViewと同時に継承．
  参考:
    Djangoの認証システムを使用する | Django ドキュメント | Django
    https://docs.djangoproject.com/ja/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
  """
  # モデルに定義された作成者のメンバ変数名
  author_field = "author"

  def test_func(self):
    obj = self.get_object()
    user = getattr(obj, self.author_field)
    return user == self.request.user

