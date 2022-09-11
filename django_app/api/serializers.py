from threading import Thread
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class ThreadColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadColor
        fields = '__all__'

class UserThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserThread
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'