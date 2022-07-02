from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreateForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'