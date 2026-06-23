from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from reputation.models import Profile


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("username", type=str, nargs="?")
        parser.add_argument("password", type=str, nargs="?")
        parser.add_argument("first_name", type=str, nargs="?")
        parser.add_argument("last_name", type=str, nargs="?")

    def handle(self, *args, **options):
        username = options.get("username")
        password = options.get("password")
        first_name = options.get("first_name")
        last_name = options.get("last_name")

        if all(v is None for v in [username, password, first_name, last_name]):
            bob = User.objects.create_user(username="Bob", password="123")
            admin = User.objects.create_superuser(username="admin", password="123")

            Profile.objects.create(user=bob, first_name="Bob", last_name="Bob")
            Profile.objects.create(user=admin, first_name="Admin", last_name="Admin")
            return

        if any(v is None for v in [username, password, first_name, last_name]):
            raise CommandError("All fields are required")

        else:
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(
                user=user, first_name=first_name, last_name=last_name
            )
