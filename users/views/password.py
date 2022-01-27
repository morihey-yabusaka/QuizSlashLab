from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import *

from ..forms import PassWordChangeForm, PassWordResetForm


class PassWordChangeView(LoginRequiredMixin, PasswordChangeView):
  template_name = 'password/change.html'
  form_class = PassWordChangeForm

  def get_success_url(self) -> str:
    return reverse('app:userpage', kwargs={'slug': self.request.user.username}) + '?state=password_change'

password_change_view = PassWordChangeView.as_view()


class PassWordResetView(PasswordResetView):
  template_name = 'password/reset.html'
  success_url = reverse_lazy('users:password_reset_done')
  form_class = PassWordResetForm
  subject_template_name = 'mail/registration/password_reset_subject.txt'
  email_template_name = 'mail/registration/password_reset_message.html'

password_reset_view = PassWordResetView.as_view()


class PassWordResetDoneView(PasswordResetDoneView):
  template_name = 'password/reset_done.html'

password_reset_done_view = PassWordResetDoneView.as_view()


class PassWordResetConfirmView(PasswordResetConfirmView):
  template_name = 'password/reset_confirm.html'
  success_url = reverse_lazy('users:password_reset_complete')

password_reset_confirm_view = PassWordResetConfirmView.as_view()


class PassWordResetCompleteView(PasswordResetCompleteView):
  template_name = 'password/reset_complete.html'

password_reset_complete_view = PassWordResetCompleteView.as_view()