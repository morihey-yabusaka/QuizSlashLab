from django.utils import timezone
from django.db.models import *
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from uuid import uuid4


class User(AbstractBaseUser, PermissionsMixin):
  username_validater = UnicodeUsernameValidator()

  username = TextField(
    "ユーザ名",
    max_length=32,
    unique=True,
    help_text="32文字以下の英数字、@/./+/-/_のみ使用できます。",
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
    error_messages={
      "unique": "このメールアドレスは既に使用されています。"
    }
  )

  is_staff = BooleanField(
    "権限ステータス",
    help_text="これを選択すると、スタッフとして管理権限が付与されます。",
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
  REQUIRED_FIELD = ['email', ]

  class Meta:
    verbose_name = 'ユーザ'
    verbose_name_plural = 'ユーザー'

