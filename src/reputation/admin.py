from django.contrib import admin

from reputation.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
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
