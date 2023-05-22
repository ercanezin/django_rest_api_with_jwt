from rest_framework import status, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Logs
from .serializers import LogsSerializer


class LogsApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        queryset = Logs.objects.all()
        data = queryset.filter(user=user_id)
        serializer = LogsSerializer(data, many=True)
        response = {
            "status": status.HTTP_200_OK,
            "message": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
