from rest_framework.serializers import ModelSerializer
from apps.models import Rule

class RuleSerializer(ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'
