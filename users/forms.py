from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User

class SignupForm(UserCreationForm):
  """
  サインアップ用のフォーム．
  usernameと二つのパスワードを加える．
  """

  class Meta:
    model = User
    fields = ['username']

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['placeholder'] = field.label


class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['placeholder'] = field.label


