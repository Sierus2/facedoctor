from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import ClientForm, ServiceClientForm
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


# class ServiceDetail(DetailView):
#     model = Service
#     template_name = 'landing/service_detail.html'

def serviceDetail(request, slug):
    serviceClient = Service.objects.get(slug=slug)
    if request.method == 'POST':
        name = request.POST.get('name', "")
        age = request.POST.get('age', "")
        phoneNumber = request.POST.get('phoneNumber', "")
        createClient = ServiceClient(service_id=serviceClient.pk, name=name, age=age, phoneNumber=phoneNumber)
        createClient.save()
    return render(request, 'landing/service_detail.html', {"object": serviceClient})


class PostIndex(ListView):
    model = Post
    template_name = 'landing/blog.html'


def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
        Q(translations__title__icontains=query) | Q(translations__body__icontains=query)
    )
    return render(request, 'landing/search.html', {'search_obj': search_obj})


def post_detail(request, slug):
    posts = Post.objects.get(slug__iexact=slug)
    return render(request, 'landing/blog_detail.html', {'post': posts})


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
    context = {"clients": clients, "form": form}
    return render(request, 'landing/gift.html', context)


class ClientCreateView(CreateView):
    model = Client
    template_name = 'landing/gift.html'
    form_class = ClientForm
    success_url = '/konkurs'
