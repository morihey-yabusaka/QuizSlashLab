from django.core.management.base import BaseCommand

from ...models import Quiz


class Command(BaseCommand):
  def handle(self, *args, **options):
    todays = Quiz.objects.publish().todays()
    not_todays = Quiz.objects.publish().not_todays()

    for t in todays:
      t.is_todays_question = False
      t.save()

    tomorrows = not_todays.order_by('?')[0]
    tomorrows.is_todays_question = True
    tomorrows.save()