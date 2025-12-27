from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from users.models import User




class RegisterUserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = User
        fields = 'first_name','last_name', 'email', 'password', 'confirm_password'

    def validate(self, values):
        if values.get('password') != values.get('confirm_password'):
            raise ValidationError({'Confirm password': 'passwords does not match!'})
        values.pop('confirm_password', None)
        return values

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password,**validated_data)
        return user

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name','last_name'

class ChangePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True, label="Old Password")
    new_password = CharField(write_only=True)
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = 'password', 'new_password', 'confirm_password'

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('confirm_password'):
            raise ValidationError({"confirm_password": "Passwords do not match"})
        return attrs

    def update(self, instance, validated_data):
        old_password = validated_data.get('password')
        if not instance.check_password(old_password):
            raise ValidationError({"password": "Old password is incorrect"})
        instance.set_password(validated_data.get('new_password'))
        instance.save()

        return Response({"message": "Password updated successfully"},status=status.HTTP_200_OK)
