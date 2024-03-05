from rest_framework import viewsets, permissions
from .models import Departman, Personel
from .serializers import DepartmanSerializer, PersonelSerializer
from .permissions import IsAdminOrReadOnly, IsAdminUser

class DepartmanViewSet(viewsets.ModelViewSet):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAdminOrReadOnly]

class PersonelViewSet(viewsets.ModelViewSet):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsAdminUser]