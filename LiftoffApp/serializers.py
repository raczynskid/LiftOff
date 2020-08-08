from rest_framework import serializers
from .models import *


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'


class LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
