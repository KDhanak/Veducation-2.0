from django.contrib.auth.backends import ModelBackend
from core.models import Account

class AccountBackendUsingEmail(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Account.objects.get(email=username)
        except Account.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None
