from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import ClientForm
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


def clietList(request):
    clients = Client.objects.all()
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/konkurs')
    context = {"clients": clients, "form":form}
    return render(request, 'landing/gift.html', context)


class ClientCreateView(CreateView):
    model = Client
    template_name = 'landing/gift.html'
    form_class = ClientForm
    success_url = '/konkurs'

# class GiftIndex(ListView):
#     model = Client
#     template_name = 'landing/gift.html'
