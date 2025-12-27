from django.urls import path
from apps.views import RuleViewSet

urlpatterns = [
    path('rules/', RuleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('rules/<int:pk>/', RuleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]
