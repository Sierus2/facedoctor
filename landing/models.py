from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(title, id):
    return django_slugify(''.join(alphabet.get(w, w) for w in title.lower()))


# Create your models here.
class Category(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=255),
        meta_d=models.CharField(_("Meta description"), max_length=255),
        meta_k=models.CharField(_("Meta keywords"), max_length=255),
        body=models.TextField(_("Body")),
    )
    created_date = models.DateTimeField(verbose_name=_('Yaratgan vaqti'), null=True, auto_now=True)
    updated_date = models.DateTimeField(verbose_name=_('Tahrirlangan vaqti'), null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.title


class Service(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=255),
        meta_d=models.CharField(_("Meta description"), max_length=255),
        meta_k=models.CharField(_("Meta keywords"), max_length=255),
        body=models.TextField(_("Body")),
        short_desc=models.TextField(_("Short Desc")),
    )
    slug = models.SlugField(null=True, blank=True)
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    category = models.ForeignKey('landing.Category', on_delete=models.CASCADE, related_name='service_to_category')
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated At'), null=True, blank=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, self.id)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/service/%s/" % self.slug


class FAQ(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(_("Title"), max_length=255),
        answer=models.TextField(_("Body")),
    )
    service = models.ForeignKey('landing.Service', on_delete=models.CASCADE, related_name='faq_to_service')

    def __str__(self):
        return self.question


class Region(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Viloyat nomi"), max_length=255),
    )

    def __str__(self):
        return self.title


class District(TranslatableModel):  # tuman
    translations = TranslatedFields(
        title=models.CharField(_("Tuman nomi"), max_length=255),
    )
    region = models.ForeignKey('landing.Region', on_delete=models.SET_NULL, null=True,
                               related_name='district_to_region')

    def __str__(self):
        return self.title


class Client(models.Model):  # mijoz
    name = models.CharField(_("F.I.O"), max_length=255)
    phone = models.CharField(_("Telefon raqami"), max_length=15) #, unique=True
    district = models.ForeignKey('landing.District', on_delete=models.SET_NULL, null=True,
                                 related_name='client_to_district')
    region = models.ForeignKey('landing.Region', on_delete=models.SET_NULL, null=True, related_name='client_to_region')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
