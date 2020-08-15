from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

from.serializer import Serializer

User = get_user_model()

class AuthAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"mess":"user is already authenticated"})
        data = request.data
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        qs = User.objects.filter(Q(email__iexact=username) | Q(username__iexact=username)).distinct()
        user_obj = qs.first()
        if qs.count() == 1:
            user = user_obj
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response)
        return Response({"details":"Invalid credentials"}, status=401)
        
        
class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]    
    serializer_class =   Serializer
    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}
    
  
# class RegisterApiView(APIView):
#     permission_classes = [permissions.AllowAny]
    
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return Response({"mess":"You have register already and authenticated"})
#         data = request.data
#         username = data.get("username")
#         email = data.get("email")
#         password = data.get("password")
#         password2 = data.get("password2")
#         qs = User.objects.filter(Q(email__iexact=username) | Q(username__iexact=username))
#         if password != password2:
#             Response({"password":"password must match"}, status=401)
#         if qs.exists():
#             return Response({"detail":"user already exist"})
#         else:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(token, user, request=request)
#             return Response({"detail":"Thanks for registering, Please verify your email"}, status=201)
#         return Response({"details":"Invalid request"}, status=400)




    