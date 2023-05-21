from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
 
from .helpers import *
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'status': status.HTTP_201_CREATED}
            return Response(res, status=status.HTTP_201_CREATED)

        res = {'status': status.HTTP_400_BAD_REQUEST, 'data': serializer.errors}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    """This api will handle login and generate access and refresh token for authenticate user."""

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                res_data = get_tokens_for_user(User.objects.get(username=username))
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "data": res_data
                }
                logged_in_success(user, request)

                return Response(response, status=status.HTTP_200_OK)
            else:
                logged_in_failed(serializer, request)
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid Email or Password",
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        logged_in_failed(serializer, request)
        response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "bad request",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
