from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *


# Create your views here.
class Home(ListView):
    model = Service
    template_name = 'landing/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     some_data = Product.objects.all()
    #     context.update({'some_data': some_data})
    #     return context


class ServiceIndex(ListView):
    model = Service
    template_name = 'landing/service.html'


class ServiceDetail(DetailView):
    model = Service
    template_name = 'landing/service_detail.html'


class AboutIndex(TemplateView):
    template_name = 'landing/about.html'


class ClientCreateView(CreateView):
    model = Client
    fields = ['name']


class GiftIndex(ListView):
    model = Client
    template_name = 'landing/gift.html'
