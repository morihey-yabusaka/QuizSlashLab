from django.db.models import *
from django.core.validators import *

from model_utils import FieldTracker

from users.models import User


class QuizQuerySet(QuerySet):
  def publish(self):
    return self.filter(is_publish=True)

  def todays(self):
    return self.filter(is_todays_question=True)

  def not_todays(self):
    return self.filter(is_todays_question=False)


class Quiz(Model):
  author = ForeignKey(User, on_delete=SET_DEFAULT,  default='QUIZ MAN')
  #THINK: max_length=255 妥当？
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


  # THINK: updated_at auto_now -> 問題内容が変更された時のみ更新 auto_now:下書きから出題された時も更新される
  created_at = DateTimeField('作成日時', auto_now_add=True)
  updated_at = DateTimeField('更新日時', auto_now=True)

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
    help_text='出題時のルールで定められた回答の権利が埋まり、ボタンを押す権利を無くした人数。'
  )
  n_correct = PositiveIntegerField(
    '正答人数',
    default=0,
    help_text='会問した人のうち、正答した人数。'
  )
  n_uncorrect = PositiveIntegerField(
    '誤答人数',
    default=0,
    help_text='会問した人のうち、誤答した人数。'
  )
  n_checked = PositiveIntegerField(
    '詳細閲覧回数',
    default=0,
    help_text='この問題の詳細画面を確認した人数。'
  )
  is_draft = BooleanField(
    '下書き',
    default=False,
    help_text='選択しているなら、下書きです。'
  )
  is_publish = BooleanField(
    '公開',
    default=True,
    help_text='選択しているなら、公開されています。管理者のみ変更可能。強制的に非公開に変更する場合にチェックを外す。'
  )
  is_official = BooleanField(
    '公式',
    default=False,
    help_text='選択しているなら、公式問題です。'
  )

  is_todays_question = BooleanField(
    '今日の一問',
    default=False,
    help_text='選択されていたら、今日の一問に表示されます。複数選択されていても、indexでは一問のみ表示されます。'
  )

  objects = QuizQuerySet.as_manager()

  question_tracker = FieldTracker(fields=['question']) # questionの変更を検知する

  def __str__(self) -> str:
      return "A: " + self.answer + " - Q: " + self.question

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    slashes = Slash.objects.filter(quiz=self)
    if self.question_tracker.changed() or slashes.count() == 0:
      for i in range(len(self.question)):
        Slash.objects.create(
          quiz=self,
          slash_position=i+1,
          before_all=self.question[:i+1],
          before_just=self.question[i]
        )
      if self.question_tracker.changed():
        for slash in slashes:
          slash.delete()


class ActionManager(Manager):
  """
  add chain to goodquiz and betamon objects
  ex)
  gq_quiz_list = GoodQuiz.objects.quiz()
  beta_user_list = BetaMon.objects.user()
  """

  def quiz(self):
    """
    return:
      list of quiz object
    """
    return [gq.quiz for gq in self.get_queryset()]

  def user(self):
    """
    return:
      list of user object
    """
    return [gq.user for gq in self.get_queryset()]


class BetaMon(Model):
  quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name='betamon')
  user = ForeignKey(User, on_delete=CASCADE, related_name='betamon')
  created_at = DateTimeField(auto_now_add=True)
  objects = ActionManager()


class GoodQuiz(Model):
  quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name='good_quiz')
  user = ForeignKey(User, on_delete=CASCADE, related_name='good_quiz')
  created_at = DateTimeField(auto_now_add=True)
  objects = ActionManager()


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
    help_text='このスラッシュでボタンを押した人のうち、正答した人数。'
  )
  n_uncorrect = PositiveIntegerField(
    '誤答人数',
    default=0,
    help_text='このスラッシュでボタンを押した人のうち、誤答した人数。'
  )

  def __str__(self):
    return str(self.quiz) + '-' + str(self.slash_position) + ' ' + self.before_just
