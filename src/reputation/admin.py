from django.contrib import admin

from reputation.models import LogsTransfers, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "reputation_balance",
        "created_at",
        "updated_at",
        "user",
    ]
    list_display_links = [
        "first_name",
        "last_name",
    ]
    list_editable = ["reputation_balance"]


@admin.register(LogsTransfers)
class LogsTransfersAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "from_user",
        "to_user",
        "reputation",
        "created_at",
    ]
