from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from reputation.models import Profile
from reputation.repository import Repository
from reputation.serializers import ProfileSerializer, TransferSerializer
from reputation.service import ReputationService


class ListProfileAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DetailProfileAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "id"


class TransferReputationAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = TransferSerializer

    def put(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = ReputationService(serializer)
        service.perform_transfer()
        data = service.get_response_data()
        return Response(status=status.HTTP_200_OK, data=data)
