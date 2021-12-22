from django.db.models import *
from django.core.validators import *

import json

from users.models import User

class Quiz(Model):
  author = ForeignKey(User, on_delete=SET_DEFAULT,  default='QUIZ MAN')
  question = TextField(
    '問題文',
    max_length=255,
    null=False,
    help_text="255文字まで使用できます。"
  )
  answer = CharField(
    '解答',
    max_length=255,
    null=False,
    help_text="255文字まで使用できます。"
  )
  answer_yomi = CharField(
    '解答かな',
    max_length=255,
    null=False,
    help_text="全角ひらがな255文字まで使用できます。",
    validators=[RegexValidator(
      regex=r'^[ぁ-ん]',
      message='全角のひらがなで入力してください。'
    )]
  )

  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)

  n_encount = PositiveIntegerField(
    '会問人数',
    default=0,
    help_text='問題が出題された人数。'
  )
  n_pushed = PositiveIntegerField(
    '獲答権人数',
    default=0,
    help_text='ボタンを押して回答の権利を得た人数。'
  )
  n_through = PositiveIntegerField(
    '棄答権人数',
    default=0,
    help_text='ボタンを押す権利があっても押さなかった人数。'
  )
  n_stolen = PositiveIntegerField(
    '埋答人数',
    default=0,
    help_text='出題時のルールで定められた回答の権利が埋まり，ボタンを押す権利を無くした人数。'
  )
  n_correct = PositiveIntegerField(
    '正答人数',
    default=0,
    help_text='会問した人のうち，正答した人数。'
  )
  n_uncorrect = PositiveIntegerField(
    '誤答人数',
    default=0,
    help_text='会問した人のうち，誤答した人数。'
  )
  n_checked = PositiveIntegerField(
    '詳細閲覧回数',
    default=0,
    help_text='この問題の詳細画面を確認した人数。'
  )
  is_draft = BooleanField(
    '下書き状況',
    default=True,
    help_text='選択しているなら，下書きです。'
  )
  is_publish = BooleanField(
    '公開状況',
    default=False,
    help_text='選択しているなら，公開されています。'
  )
  is_official = BooleanField(
    '公式状況',
    default=False,
    help_text='選択しているなら，公式問題です。'
  )

  def __str__(self) -> str:
      return "A: " + self.answer + " - Q: " + self.question

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    slashes = Slash.objects.filter(quiz=self)
    if slashes.count() != len(self.question):
      for i in range(len(self.question)):
        Slash.objects.create(
          quiz=self,
          slash_position=i+1,
          before_all=self.question[:i+1],
          before_just=self.question[i]
        )


class BetaMon(Model):
  quiz = OneToOneField(Quiz, on_delete=CASCADE)
  user = OneToOneField(User, on_delete=CASCADE)
  created_at = DateTimeField(auto_now_add=True)


class GoodQuiz(Model):
  quiz = OneToOneField(Quiz, on_delete=CASCADE)
  user = OneToOneField(User, on_delete=CASCADE)
  created_at = DateTimeField(auto_now_add=True)


class Slash(Model):
  quiz = ForeignKey(
    Quiz,
    on_delete=CASCADE,
  )
  slash_position = PositiveSmallIntegerField(
    'スラッシュ箇所',
    help_text='n文字目直後のスラッシュ'
  )
  before_all = TextField(
    'スラッシュ文',
    help_text='スラッシュ直前までの問題文'
  )
  before_just = CharField(
    'スラッシュ文字',
    max_length=1,
    help_text='スラッシュ直前の一文字'
  )
  n_push = PositiveIntegerField(
    '押ボタン人数',
    default=0,
    help_text='このスラッシュでボタンが押された数'
  )
  n_correct = PositiveIntegerField(
    '正答人数',
    default=0,
    help_text='このスラッシュでボタンを押した人のうち，正答した人数。'
  )
  n_uncorrect = PositiveIntegerField(
    '誤答人数',
    default=0,
    help_text='このスラッシュでボタンを押した人のうち，誤答した人数。'
  )
