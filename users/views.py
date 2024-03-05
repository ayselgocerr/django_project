from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer, UserSerializer

from rest_framework.generics import ListAPIView


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# ----------- User Logout Function ------------------



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout

@api_view(['POST'])
def logout(request):
    try:
        # Kullanıcı giriş yapmışsa, auth token'ı silebiliriz.
        request.user.auth_token.delete()
    except (AttributeError, Token.DoesNotExist):
        # Kullanıcı giriş yapmamışsa veya token bulunamadıysa burası çalışır.
        pass

    # Django logout fonksiyonunu çağırarak oturumu kapat.
    logout(request)
    return Response({"message": "User logged out successfully"})

