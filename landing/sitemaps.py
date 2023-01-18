from django.contrib import sitemaps
from django.urls import reverse

from landing.models import Service


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        services = Service.objects.all().order_by('-updated_at')
        return ['home', 'service', 'about']

    def location(self, item):
        return reverse(item)


class ServiceViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        services = Service.objects.all().order_by('-updated_at')
        return services

    def lastmod(self, obj):
        return obj.updated_at