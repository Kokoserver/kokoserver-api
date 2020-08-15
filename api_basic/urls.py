from django.urls import path
from .views import ArticleEndPointApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ArticleEndPointApi, basename="article" )

# urlpatterns = [
#      path("",  ViewSetApi.as_view()),
#     path("<int:pk>/",  ArticleDetail.as_view()),
#     # path("<int:id>/", ArticleDetailApiView.as_view()),
#     # path("article/<int:id>", article_detail )
# ]

urlpatterns = router.urls