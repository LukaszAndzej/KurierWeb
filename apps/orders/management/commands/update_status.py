from django.core.management.base import BaseCommand
from apps.orders.tasks import update_order_status

class Command(BaseCommand):
    help = 'Uruchamia proces automatycznej zmiany statusów zamówień'

    def handle(self, *args, **kwargs):
        self.stdout.write('Uruchamianie zmiany statusów...')
        update_order_status()
