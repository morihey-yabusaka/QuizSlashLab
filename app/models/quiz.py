from django.db.models import *

class Quiz(Model):
  question = TextField(max_length=255)
  author = ForeignKey()
  answer = CharField(max_length=255)
  answer_yomi = CharField(max_length=255)
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)
  seen = IntegerField()


  def __str__(self) -> str:
      return self.question