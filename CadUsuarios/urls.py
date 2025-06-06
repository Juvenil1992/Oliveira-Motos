from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include

urlpatterns = [
    path('login_usuario', views.login_usuario, name='login_usuario'),
]