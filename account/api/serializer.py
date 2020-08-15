import datetime
from django.contrib.auth import get_user_model
from  rest_framework import serializers
from django.conf import settings
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

from django.utils import timezone

# expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']

User = get_user_model()

class Serializer(serializers.ModelSerializer):
    password  = serializers.CharField(style={"input_type":"password"}, write_only=True)
    password2  = serializers.CharField(style={"input_type":"password"}, write_only=True)
    token      = serializers.SerializerMethodField(read_only=True)
    expire     = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)
    # token_response = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
            "token",
            "expire",
            "message"
            
            # "token_response"
            
        ]
    extra_kwargs = {"password": {"write_only":True}}
    
    def validate(self, data):
        pw = data.get("password")
        pw2 = data.get("password2")
        if pw != pw2:
            raise serializers.ValidationError("Passwword must match")
        return data
    
    def create(self, validate_data):
        user_obj = User(username=validate_data.get("username"),  email=validate_data.get("email"))
        user_obj.set_password(validate_data.get("password"))
        user_obj.is_active = False
        user_obj.save()
        return user_obj
    
    def get_token(self, obj):
         user = obj
         payload = jwt_payload_handler(user)
         token = jwt_encode_handler(payload)
         return token
     
    def get_message(self, obj):
        return "Thank you for regisering"
     
    # def get_token_response(self, obj):
    #     user = obj
    #     payload = jwt_payload_handler(user)
    #     token = jwt_encode_handler(payload)
    #     context = self.context
    #     response = jwt_response_payload_handler(token, user, request=context["request"])
    #     return response
     
    # def get_expire(self, obj):
    #     expire = timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    
    def validate_email(self, value):
        user_obj = User.objects.filter(email__iexact=value)
        if user_obj.exists():
            raise serializers.ValidationError("email already exist")
        return value
    
    def validate_username(self, value):
        user_obj = User.objects.filter(username__iexact=value)
        if user_obj.exists():
            raise serializers.ValidationError("User name already exist")
        return value
        