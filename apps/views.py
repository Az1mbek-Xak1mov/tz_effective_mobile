from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from apps.models import Rule
from apps.serializers import RuleSerializer

class RuleViewSet(ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAdminUser]
