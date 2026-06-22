from django.conf import settings
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    reputation_balance = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        indexes = [
            models.Index(fields=["created_at"], name="created_at_idx"),
        ]

    def __str__(self):
        return f"Profile: {self.first_name} {self.last_name}"


class LogsTransfers(models.Model):
    from_user = models.CharField(max_length=100)
    to_user = models.CharField(max_length=100)
    reputation = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transfer: {self.from_user} -> {self.to_user} ({self.reputation})"
