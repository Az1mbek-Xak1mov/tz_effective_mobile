from django.db.models import Model, ForeignKey, CASCADE, CharField, BooleanField
from users.models import User

class Rule(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='rules')
    resource = CharField(max_length=255)
    action = CharField(max_length=255)
    is_allowed = BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.resource} - {self.action} - {self.is_allowed}"
