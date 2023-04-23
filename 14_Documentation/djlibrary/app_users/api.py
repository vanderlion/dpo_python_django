from django.contrib.auth.models import User
from rest_framework import viewsets
from app_users.serializers import UserSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
