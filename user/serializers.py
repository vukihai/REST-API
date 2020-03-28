from rest_framework import serializers
from .models import User, Intent

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username', 'password','name','access_token')

class IntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intent
        fields = ('intent_name', 'quantity')