# ./in_memory_authentication/backends/in_memory_authentication_backend.py
import uuid

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class InMemoryAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Replace this silly logic with whatever you need:
        if username == "let_me_in" and password == "please":

            # Create a new user
            new_user = User(username=uuid.uuid4().__str__())
            new_user.set_unusable_password()
            new_user.save()

            return new_user
        else:
            return None
