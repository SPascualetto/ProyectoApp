from django.urls import path
from .views import RegistroPagina, UsuarioEdicion

urlpatterns = [
    path('register/', RegistroPagina.as_view(),name='register'), 
    path('editar/', UsuarioEdicion.as_view(), name='editar'),
    
    
]
