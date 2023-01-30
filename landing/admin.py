from django.contrib import admin
from django.contrib.admin import ModelAdmin
from parler.admin import TranslatableAdmin

from landing.models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['title', 'id']
    list_display_links = ['title', 'id']
    save_on_top = False


@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display = ['title', 'id']
    list_display_links = ['title', 'id']
    save_on_top = False


@admin.register(Post)
class PostAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ['title', 'id']
    list_display_links = ['title', 'id']
    save_on_top = False

@admin.register(FAQ)
class FAQAdmin(TranslatableAdmin):
    list_display = ['question', 'id']
    list_display_links = ['question', 'id']
    save_on_top = False


@admin.register(Region)
class RegionAdmin(TranslatableAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['title', ]
    save_on_top = True


@admin.register(District)
class DistrictAdmin(TranslatableAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['title', ]
    save_on_top = True


@admin.register(Client)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['name', ]
    save_on_top = True
