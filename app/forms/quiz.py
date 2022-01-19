from django.forms import ModelForm

from ..models import Quiz


class QuizForm(ModelForm):

  class Meta:
    model = Quiz
    fields = ['question', 'answer', 'answer_yomi']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['question'].widget.attrs['placeholder'] = '問題文'
    self.fields['answer'].widget.attrs['placeholder'] = '解答'
    self.fields['answer_yomi'].widget.attrs['placeholder'] = 'かいとうよみ'
