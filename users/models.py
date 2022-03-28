from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.db.models import *
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from uuid import uuid4


class UserManager(BaseUserManager):
  '''
  参考:
  Django の認証方法のカスタマイズ | Django ドキュメント | Django
  https://docs.djangoproject.com/ja/4.0/topics/auth/customizing/#a-full-example
  Django AbstractBaseUserでカスタムユーザー作成
  https://noumenon-th.net/programming/2019/12/13/abstractbaseuser/
  '''
  def create_user(self, username, password=None):
    if not username:
      raise ValueError('Users must have an username')

    user = self.model(username=username)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, username, password=None):
    user = self.create_user(
      username=username,
      password=password
    )
    user.is_staff = True
    user.is_superuser = True
    user.save()
    return user


class User(AbstractBaseUser, PermissionsMixin):
  username_validater = UnicodeUsernameValidator()

  username = CharField(
    "ユーザ名",
    max_length=16,
    unique=True,
    help_text="16文字以下の英数字、@/./+/-/_のみ使用できます。",
    validators=[username_validater],
    error_messages={
      "unique": "このユーザー名は既に使用されています。",
    }
  )

  user_id = UUIDField(
    default=uuid4,
    primary_key=True,
    editable=False
  )

  email = EmailField(
    "Eメールアドレス",
    blank=True,
    unique=True,
    null=True,
    error_messages={
      "unique": "このメールアドレスは既に使用されています。"
    }
  )

  is_superuser = BooleanField(
    "管理者ステータス",
    help_text="これを選択すると、管理者として管理権限が付与されます。",
    default=False
  )

  is_staff = BooleanField(
    "権限ステータス",
    help_text="これを選択すると、スタッフとして権限が付与されます。",
    default=False
  )

  is_active = BooleanField(
    "アクティブユーザ",
    help_text="このユーザをアクティブユーザとして扱うかどうかを指定します。アカウントを削除する際に、代わりにこの選択を解除します。",
    default=True
  )

  joined_at = DateTimeField(
    "登録日",
    default=timezone.now
  )

  objects = UserManager()

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'username'
  REQUIRED_FIELD = ['username', ]

  class Meta:
    verbose_name = 'ユーザ'
    verbose_name_plural = 'ユーザー'

