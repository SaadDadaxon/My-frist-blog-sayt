from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, views

from .serializers import ProfileSerializer
from ..models import Profile


class MyProfile(views.APIView):

    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile = Profile.objects.filter(user_id=self.request.user.id).first()
        if profile:
            serializers = ProfileSerializer(profile)
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

