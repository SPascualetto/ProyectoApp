from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render, redirect
from .models import Post, Avatar
from .forms import PostForm, EditForm, AvatarFormulario
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'home.html', {'url':avatares[0].imagen.url})
 
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            # Verificar si el usuario ya tiene un objeto Avatar
            avatar, created = Avatar.objects.get_or_create(user=u)
            avatar.imagen = miFormulario.cleaned_data['imagen']
            avatar.save()
            return redirect('home')
    else:
        miFormulario = AvatarFormulario()
    return render(request, 'agregarAvatar.html', {'miFormulario': miFormulario})

class ArticleDetailView(DetailView):
    model= Post
    template_name='detalles.html'

class AddPostView(CreateView):
    model= Post
    form_class= PostForm
    template_name='nuevoposteo.html'
  
class UpdatePostView(UpdateView):
    model=Post
    form_class= EditForm
    template_name= 'modificarposteo.html'

class DeletePostView(DeleteView):
    model=Post
    template_name= 'borrarposteo.html'
    success_url= reverse_lazy('home')

class AcercademiView(TemplateView):
    template_name= 'acercademi.html'

