from django.urls import path
from users.views import RegisterUserAPIView, UserEditProfileAPIView, ChangePasswordAPIView,UserDeleteAPIView

urlpatterns = [
    #apps
    path('user/register',RegisterUserAPIView.as_view(),name='users-register'),
    path('user/update',UserEditProfileAPIView.as_view(),name='users-update'),
    path('user/update-password',ChangePasswordAPIView.as_view(),name='users-update-password'),
    path('user/delete',UserDeleteAPIView.as_view(),name='users-delete'),
]