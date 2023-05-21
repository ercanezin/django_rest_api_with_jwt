from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 're_password', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"password": " Please enter the same password in both fields."})

        return attrs

    def create(self, validated_data):
        del validated_data['re_password']
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        res = {'status': status.HTTP_201_CREATED, 'user': user}
        return Response(res, status=status.HTTP_201_CREATED)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']
