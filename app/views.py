from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet
from django.urls import reverse_lazy
from .forms import PetForm



class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'


class PetListView(ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'app/pet_list.html'


class PetCreateView(CreateView):
    model = Pet
    fields = ['name', 'animal', 'breed', 'age', 'description', 'post_image']
    template_name = 'app/pet_create.html'

class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'app/pet_update.html'

    def get_success_url(self):
        return reverse_lazy('pet_detail', kwargs={'pk': self.object.pk})

class PetDetailView(DetailView):
    model = Pet
    template_name = 'app/pet_detail.html'
    context_object_name = 'pet'


class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'app/pet_delete.html'
    success_url = reverse_lazy('pets')

