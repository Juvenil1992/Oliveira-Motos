from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include

urlpatterns = [
    path('calculadora', views.calculadora, name='calculadora'),
    path('quem_somos', views.quem_somos, name='quem_somos'),
]