from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),

    path('konkurs/', GiftIndex.as_view(), name='gift'),
    path('about/', AboutIndex.as_view(), name='about'),
    path('service/', ServiceIndex.as_view(), name='service'),
    path('service/<str:slug>/', ServiceDetail.as_view(), name='service_detail'),
]
