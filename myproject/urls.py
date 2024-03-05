from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmanViewSet, PersonelViewSet

router = DefaultRouter()
router.register('departman', DepartmanViewSet, )
router.register('personel', PersonelViewSet, )

urlpatterns = [
    path('', include(router.urls)),
    
]