from django.urls import path
from .views import home, login_user, logout_user, register_user

urlpatterns = [
    path('', home , name='homepage'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register')

]