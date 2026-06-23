from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from reputation.views import (
    CurrentProfileAPIView,
    DetailProfileAPIView,
    ListProfileAPIView,
    TransferReputationAPIView,
)

app_name = "reputation"

urlpatterns = [
    path("profiles/", ListProfileAPIView.as_view(), name="list_profiles"),
    path("profiles/current/", CurrentProfileAPIView.as_view(), name="current_profile"),
    path("profiles/<int:id>/", DetailProfileAPIView.as_view(), name="detail_profile"),
    path("transfer/", TransferReputationAPIView.as_view(), name="transfer"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
