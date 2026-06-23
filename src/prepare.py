import os

import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "core.settings"
)
django.setup()


def prepare():
    from django.contrib.auth.models import User
    from reputation.models import Profile

    bob = User.objects.create_user(username="Bob", password="123")
    admin = User.objects.create_superuser(username="admin", password="123")

    Profile.objects.create(
        user=bob,
        first_name="Bob",
        last_name="Bob",
    )
    Profile.objects.create(user=admin, first_name="Admin", last_name="Admin")


prepare()
