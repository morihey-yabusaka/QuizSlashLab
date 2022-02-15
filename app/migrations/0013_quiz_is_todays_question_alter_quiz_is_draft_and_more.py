# Generated by Django 4.0 on 2022-02-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_betamon_quiz_alter_betamon_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_todays_question',
            field=models.BooleanField(default=False, help_text='選択されていたら、今日の一問に表示されます。', verbose_name='今日の一問'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='is_draft',
            field=models.BooleanField(default=False, help_text='選択しているなら、下書きです。', verbose_name='下書き'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='is_official',
            field=models.BooleanField(default=False, help_text='選択しているなら、公式問題です。', verbose_name='公式'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='is_publish',
            field=models.BooleanField(default=True, help_text='選択しているなら、公開されています。管理者のみ変更可能。強制的に非公開に変更する場合にチェックを外す。', verbose_name='公開'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='n_correct',
            field=models.PositiveIntegerField(default=0, help_text='会問した人のうち、正答した人数。', verbose_name='正答人数'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='n_stolen',
            field=models.PositiveIntegerField(default=0, help_text='出題時のルールで定められた回答の権利が埋まり、ボタンを押す権利を無くした人数。', verbose_name='埋答人数'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='n_uncorrect',
            field=models.PositiveIntegerField(default=0, help_text='会問した人のうち、誤答した人数。', verbose_name='誤答人数'),
        ),
        migrations.AlterField(
            model_name='slash',
            name='n_correct',
            field=models.PositiveIntegerField(default=0, help_text='このスラッシュでボタンを押した人のうち、正答した人数。', verbose_name='正答人数'),
        ),
        migrations.AlterField(
            model_name='slash',
            name='n_uncorrect',
            field=models.PositiveIntegerField(default=0, help_text='このスラッシュでボタンを押した人のうち、誤答した人数。', verbose_name='誤答人数'),
        ),
    ]
