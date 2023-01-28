from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('konkurs/', clietList, name='gift'),
    path('konkurs/', ClientCreateView.as_view(), name='create'),
    path('about/', AboutIndex.as_view(), name='about'),
    path('post/', PostIndex.as_view(), name="post"),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('search/', search_result, name="search_url"),
    path('service/', ServiceIndex.as_view(), name='service'),
    path('service/<str:slug>/', ServiceDetail.as_view(), name='service_detail'),
]
