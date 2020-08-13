import json
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics,mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from .serializer import StatusSerializer
from api.models import Status

# checking the incoming data is json
def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        valid_json = True
    except:
        valid_json = False
    return valid_json

# class StatusListSearchAPI(APIView):
#     permission_classeses = []
#     Authentication_classes = []
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)



# endpoint for details, update and delete
class StatusDetailsAPIView( 
                mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin, 
                generics.RetrieveAPIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    lookup_field     = "id"
    queryset    = Status.objects.all()
    def put(self, request, *args, **kwargs):
        print(request.user)
        return  self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
# endpoint for creating and retrieving list
class StatusAPI(mixins.CreateModelMixin, 
                generics.ListAPIView):
     
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
           qs = qs.filter(content__icontains=query)
        return qs
   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
       serializer.save(user=self.request.user)
    
    
    
    

    
# class StatusAPI(mixins.RetrieveModelMixin,
#                 mixins.CreateModelMixin,
#                 mixins.UpdateModelMixin, 
#                 mixins.DestroyModelMixin,
#                 generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#     passed_id  = None
    
#     def is_json(self,json_data):
#         try:
#            real_json = json.loads(json_data)
#            valid_json = True
#         except:
#            valid_json = False
#         return valid_json
    
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#            qs = qs.filter(content__icontains=query)
#         return qs
    
#     def get_object(self):
#         request  = self.request
#         passed_id = request.GET.get('id', None) or self.passed_id
#         queryset = self.get_queryset()
#         if passed_id is not None:
#             obj = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)
#         return obj
   
#     def get(self, request, *args, **kwargs):
#             url_passed_id = request.GET.get('id', None)
#             json_data  = {}
#             _body  = request.body
#             # data = json.loads(_body)
#             if self.is_json(_body):
#                 json_data = json.loads(_body)
#             new_passed_id = json_data.get('id', None)
#             obj = None
#             passed_id = url_passed_id or new_passed_id or None
#             self.passed_id = passed_id
#             if passed_id is not None:
#                 return self.retrieve(request, *args, **kwargs)
#             return super().get(request, *args, **kwargs)
    
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data  = {}
#         _body  = request.body
#         # data = json.loads(_body)
#         if self.is_json(_body):
#             json_data = json.loads(_body)
#         new_passed_id = json_data.get('id', None)
#         obj = None
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return  self.update(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data  = {}
#         _body  = request.body
#         # data = json.loads(_body)
#         if self.is_json(_body):
#             json_data = json.loads(_body)
#         new_passed_id = json_data.get('id', None)
#         obj = None
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return  self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data  = {}
#         _body  = request.body
#         # data = json.loads(_body)
#         if self.is_json(_body):
#             json_data = json.loads(_body)
#         new_passed_id = json_data.get('id', None)
#         obj = None
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.destroy(request, *args, **kwargs)
    
# this is the same as bellow 
# class StatusDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # lookup_field = "id"
#     queryset = Status
#     serializer_class = StatusSerializer
    
    
# class StatusDetailAPI(mixins.DestroyModelMixin, mixins.UpdateModelMixin,generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # lookup_field = "id"
#     queryset = Status
#     serializer_class = StatusSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
  
        