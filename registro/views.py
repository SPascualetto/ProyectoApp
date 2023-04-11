from django.views.generic import  UpdateView
from django.views.generic.edit import  UpdateView, FormView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import FormularioRegistroUsuario, FormularioEdicion

class RegistroPagina(FormView):
    template_name = 'registration/register.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'registration/editar.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
