from django.core.management.base import BaseCommand, CommandError
from shrinkyy.models import shrinkURL

class Command(BaseCommand):
    help = 'Refreshes all shrinkURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return shrinkURL.objects.refresh_shortcodes(items=options['items'])