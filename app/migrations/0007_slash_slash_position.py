# Generated by Django 4.0 on 2021-12-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_quiz_n_checked_alter_quiz_n_correct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slash',
            name='slash_position',
            field=models.PositiveSmallIntegerField(default=0, help_text='n文字目直後のスラッシュ', verbose_name='スラッシュ箇所'),
            preserve_default=False,
        ),
    ]
