from AppCoder import views
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AcercademiView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detalles/<int:pk>', ArticleDetailView.as_view(), name='detalles'),
    path('nuevoposteo/', AddPostView.as_view(), name='nuevoposteo'),
    path('posteo/edit/<int:pk>', UpdatePostView.as_view(), name='modificarposteo'),
    path('posteo/<int:pk>/remove', DeletePostView.as_view(), name='borrarposteo'),
    path('acercademi/', AcercademiView.as_view(), name='acercademi'),
    path('agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
]

