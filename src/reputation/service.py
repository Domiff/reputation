from reputation.repository import Repository


class ReputationService:
    def __init__(self, serializer):
        self.repo = Repository()
        self.serializer = serializer

    def perform_transfer(self) -> None:
        self.repo.transfer(
            self.serializer.validated_data["from_user"],
            self.serializer.validated_data["to_user"],
            self.serializer.validated_data["reputation"],
        )

    def get_response_data(self) -> dict:
        data = {
            "from_user": self.repo.get_user(self.serializer.validated_data["from_user"]).username,
            "to_user": self.repo.get_user(self.serializer.validated_data["to_user"]).username,
            "reputation": self.serializer.validated_data["reputation"],
        }
        return data
