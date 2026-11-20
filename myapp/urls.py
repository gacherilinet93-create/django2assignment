from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, welcome

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', welcome, name='welcome'),
    path('', include(router.urls)),
]