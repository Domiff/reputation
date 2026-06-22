from rest_framework import serializers

from reputation.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "reputation_balance",
            "created_at",
            "updated_at",
            "user",
        ]


class TransferSerializer(serializers.Serializer):
    from_user = serializers.IntegerField(allow_null=False)
    to_user = serializers.IntegerField(allow_null=False)
    reputation = serializers.IntegerField(min_value=1, allow_null=False)

    def validate(self, attrs):
        from_user = attrs["from_user"]
        to_user = attrs["to_user"]
        if from_user == to_user:
            raise serializers.ValidationError(
                "You cannot transfer reputation to yourself"
            )
        user = self.context["request"].user
        if user.id != from_user:
            raise serializers.ValidationError(
                "You can only transfer reputation from your own profile"
            )
        return attrs
