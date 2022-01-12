from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['placeholder'] = field.label