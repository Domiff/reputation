from django.contrib.auth.models import User
from django.db.transaction import atomic

from reputation.models import LogsTransfers, Profile


class Repository:
    @staticmethod
    def get_user(pk: int):
        return User.objects.get(pk=pk)

    @staticmethod
    def get_profile(user_id: int):
        return Profile.objects.filter(user=user_id)

    @atomic
    def transfer(self, from_user: int, to_user: int, reputation: int):
        from_user_balance = list(
            self.get_profile(from_user).values_list("reputation_balance", flat=True)
        )
        to_user_balance = list(
            self.get_profile(to_user).values_list("reputation_balance", flat=True)
        )
        self.get_profile(from_user).update(
            reputation_balance=from_user_balance[0] - reputation
        )
        self.get_profile(to_user).update(
            reputation_balance=to_user_balance[0] + reputation
        )

    @staticmethod
    def record_transfer_reputation(from_user: str, to_user: str, reputation: int):
        LogsTransfers.objects.create(
            from_user=from_user, to_user=to_user, reputation=reputation
        )
