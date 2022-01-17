from datetime import date
from django.core.management.base import BaseCommand, CommandError
from api.views import get_weather_forecast


class Command(BaseCommand):
    help = """
        python manage.py weather_forecast -d <date> -c <Country_code>
        date: 2021-26-05
        country_code: CZ\n
        -d date (YYYY-MM-DD)
        -c Country code (CZ, UK, IN)
        returns weather-forecast for date
        """

    def add_arguments(self, parser):
        parser.add_argument('-d', nargs='+', type=str)
        parser.add_argument('-c', nargs="+", type=str)

    def handle(self, *args, **options):
        # print(options)
        val = get_weather_forecast(options['d'], options['c'])

        self.stdout.write(self.style.SUCCESS('%s' % val))