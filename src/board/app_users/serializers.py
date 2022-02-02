from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.HyperLinked):

    class Meta:
        model = User
        fields = ['id', 'is_staff', 'username', 'email']