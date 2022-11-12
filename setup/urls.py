
from django.contrib import admin
from django.urls import path,include

# seguimentando as responsabilidades/ tudo da galeria vai ficar em galeria/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), 
]
