# ./in_memory_authentication/backends/in_memory_authentication_backend.py
import uuid

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class InMemoryAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        return self.find_user(username, password)

    # Replace this silly logic with something better, such as an API call to
    # an identity provider:
    def find_user(self, username, password):
        if username == "let_me_in" and password == "please":
            user_klass = get_user_model()
            new_user = user_klass(username=uuid.uuid4().__str__())
            new_user.set_unusable_password()
            new_user.save()
            return new_user
        else:
            return None
