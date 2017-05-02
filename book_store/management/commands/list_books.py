from django.core.management.base import BaseCommand, CommandError

from ...models import Book


class Command(BaseCommand):
    help = 'List all books'

    def add_arguments(self, parser):
        parser.add_argument(
            '--order',
            dest='order',
            default=False,
            help='Order books list by asc or desc',
        )

    def handle(self, *args, **options):
        queryset = Book.objects.all()

        if options['order']:
            if options['order'] == 'asc':
                queryset = queryset.order_by('published_date')
            if options['order'] == 'desc':
                queryset = queryset.order_by('-published_date')

        for book in queryset:
            print(book)
