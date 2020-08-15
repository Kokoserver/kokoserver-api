import io
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
# from rest_framework import generics, mixins
# from rest_framework.views import APIView
from rest_framework import permissions, authentication
from .serializer import ArticleSerializer
from .models import Article as ArticleModel
from django.shortcuts import get_object_or_404

# Create your views here.

# class ArticleList(generics.ListCreateAPIView):
#     queryset = ArticleModel.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ArticleModel.objects.all()
#     serializer_class = ArticleSerializer
    
class ArticleEndPointApi(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset  = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    def get_byte(self):
        stream = io.BytesIO(self.request.body)
        data = JSONParser().parse(stream)
        id = data.get("id", None)
        return id
    
    def get_queryset(self):
            try:
                id = self.get_byte()
                if id is not None:
                    # i will get single object but to make it queryset i will have to make it an array
                    qs = ArticleModel.objects.filter(pk=id)
                    return qs
            except:
                searchPrarams = self.request.query_params.get("q", None)
                qs = ArticleModel.objects.all()
                if searchPrarams is not None:
                    qs = ArticleModel.objects.filter(title__icontains=searchPrarams)
                return qs 
        
        
    def get_object(self):
        try:
            id = self.get_byte()
            if id is not None:
                obj = get_object_or_404(ArticleModel, pk=id)
                return obj
        except:
            id = self.kwargs.get("pk")
            obj = get_object_or_404(ArticleModel, pk=id)
            return obj
    def perform_create(self, serializer):
        user = get_user_model()
        return serializer.save(author=self.request.user.username)

        

      
    
    
# class ViewSetApi(ViewSet):
#     def get_byte(self, request):
#        stream = io.BytesIO(request.body)
#        data = JSONParser().parse(stream)
#        id = data.get("id", None)
#        return id
       
#     def get_queryset(self):
#             searchPrarams = self.request.query_params.get("q", None)
#             qs = ArticleModel.objects.all()
#             if searchPrarams is not None:
#                 qs = ArticleModel.objects.filter(title__icontains=searchPrarams)
#             return qs
        
#     def get_object(self, request=None):
#         id = self.get_byte(request)
#         if id is not None:
#             obj = get_object_or_404(ArticleModel, pk=id)
#             return obj
        
#     def list(self, request):
#         try:
#                 obj = self.get_object(request=request)
#                 if obj is not None:
#                     serilaizer = ArticleSerializer(obj)
#                     return Response(serilaizer.data, status=status.HTTP_200_OK)
#         except:
#             pass
#         qs = self.get_queryset()
#         serilaizer = ArticleSerializer(qs, many=True)
#         print(self.request.stream)
#         return Response(serilaizer.data, status=status.HTTP_200_OK)
    
#     def retrieve(self, request, pk=None):
#         obj = get_object_or_404(ArticleModel, pk=pk)
#         serializer = ArticleSerializer(obj)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         qs = get_object_or_404(ArticleModel, pk=pk)
#         serializer = ArticleSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      
          
      
          

# class ArticleDetailApi(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     serializer_class   = ArticleSerializer
#     queryset    = ArticleModel.objects.all()
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
    
# class ArticleListApi(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#        serializer_class = ArticleSerializer
#        queryset = ArticleModel.objects.all()
#        def get(self, request, *args, **kwargs):
#            return self.list(request, *args, **kwargs)
       
#        def post(self, request, *args, **kwargs):
#            return self.create(request, *args, **kwargs)
   
    
    


# class ArticleDetailApiView(APIView):
#     def get_object(self, id):
#         try:  
#             return ArticleModel.objects.get(id=id) 
#         except ArticleModel.DoesNotExist or AttributeError:
#                 return Response({"detail":"sorry article is not found"}, status= status.HTTP_404_NOT_FOUND)
    
           
#     def get(self, request, id):
#             article = self.get_object(id)
#             serializer = ArticleSerializer(article)
#             return Response(serializer.data, status=status.HTTP_200_OK)  
        
#     def put(self, request, id):
#             article = self.get_object(id)
#             serializer = ArticleSerializer(article, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, id):
#          article = self.get_object(id)
#          article.delete()
#          return Response({"detail":"deleted successfully"}, status=status.HTTP_200_OK)
    
        
        
# class ArticleApiView(APIView):
#     def get(self, request):
#         try:
#             streem = io.BytesIO(request.body)
#             print(request.data)
#             data = JSONParser().parse(streem)
#             obj_id = data.get("id",None)
#         except:
#             qs = ArticleModel.objects.all()
#             serializer = ArticleSerializer(qs, many=True)
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         if obj_id is not None:
#             try:
#                 obj = ArticleModel.objects.get(id=obj_id)
#             except ArticleModel.DoesNotExist:
#                 return Response({"detail":"sorry article is not found"}, status= status.HTTP_404_NOT_FOUND)
#             serializer = ArticleSerializer(obj)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#          serializer = ArticleSerializer(data=request.data)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#          else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         



















# @api_view(["GET", "POST"])
# def article(request):
#     if request.method == "GET":
#         obj_id = None
#         try:
#             streem = io.BytesIO(request.body)
#             print(request.data)
#             data = JSONParser().parse(streem)
#             obj_id = data.get("id",None)
#         except:
#             qs = ArticleModel.objects.all()
#             serializer = ArticleSerializer(qs, many=True)
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         if obj_id is not None:
#             try:
#                 obj = ArticleModel.objects.get(id=obj_id)
#             except ArticleModel.DoesNotExist:
#                 return Response({"detail":"sorry article is not found"}, status= status.HTTP_404_NOT_FOUND)
#             serializer = ArticleSerializer(obj)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response({"detail":"sorry article can't be empty "}, status=status.HTTP_404_NOT_FOUND)

# @api_view(["PUT", "GET", "DELETE"])
# def article_detail(request, id):
#         try:
#                article = ArticleModel.objects.get(id=id)
#         except ArticleModel.DoesNotExist:
#             return Response({"detail":"article not found"}, status=status.HTTP_400_BAD_REQUEST)
#         if request.method == "GET":
#             serializer = ArticleSerializer(article)
#             return Response(serializer.data)
#         elif request.method == "PUT":
#             streem = io.BytesIO(request.body)
#             data = JSONParser().parse(streem)
#             id = data.get("id")
#             article = ArticleModel.objects.get(id=id)
#             serializer = ArticleSerializer(article, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == "DELETE":
#             streem = io.BytesIO(request.body)
#             data = JSONParser().parse(streem)
#             id = data.get("id")
#             try:
#                 article = ArticleModel.objects.get(id=id)
#             except ArticleModel.DoesNotExist:
#                 return Response({"detail":"sorry article is not found"}, status= status.HTTP_404_NOT_FOUND)
#             article.delete()
#             return Response({"detail":"deleted successfully"}, status=status.HTTP_200_OK)
        
        