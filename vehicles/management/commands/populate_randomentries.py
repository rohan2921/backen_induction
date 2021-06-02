from django.core.management.base import BaseCommand, CommandError
from ...models import RandomEntries


class Command(BaseCommand):
    help = 'Add new entry to RandomEntries model'

    def add_arguments(self, parser):
        parser.add_argument('value', nargs='+', type=str)

    def handle(self, *args, **options):
        for value in options['value']:
            obj = RandomEntries.objects.create(flag=value)
            obj_id = obj.id
            self.stdout.write(self.style.SUCCESS('Successfully added entry with id "%s"' % obj_id))
