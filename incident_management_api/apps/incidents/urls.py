from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidentViewSet, CommentViewSet

router = DefaultRouter()
router.register('incidents', IncidentViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
