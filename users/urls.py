from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterView, logout, UserListView




urlpatterns = [
    path("register/", RegisterView.as_view()), #kayıtolma endpoint i
    path('login/', views.obtain_auth_token),   #oturum açma
    path('logout/', logout),                   #oturum kapatma
    path('', UserListView.as_view()),          #kullanıcı listeleme
   
]
