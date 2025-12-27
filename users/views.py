from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import  RegisterUserSerializer, UserUpdateSerializer, \
    ChangePasswordSerializer


@extend_schema(tags=['Users'])
class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = AllowAny,

@extend_schema(tags=['Users'])
class UserEditProfileAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    http_method_names = ['patch']

    def get_object(self):
        return self.request.user

@extend_schema(tags=['Users'])
class ChangePasswordAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    http_method_names = ['put']
    def get_object(self):
        return self.request.user

@extend_schema(tags=['Users'])
class UserDeleteAPIView(DestroyAPIView):
    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response( {"message": "Account deactivated successfully. You have been logged out."},status=status.HTTP_204_NO_CONTENT)