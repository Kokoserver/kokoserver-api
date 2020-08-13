
from django.urls import path
from .views import StatusAPI, StatusDetailsAPIView

urlpatterns = [
    path('', StatusAPI.as_view()),
    path('<int:id>/', StatusDetailsAPIView.as_view()),
]