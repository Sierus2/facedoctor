import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Client


# phone_regex = re.compile(r"^9\d{12}$")


class ClientForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^9\d{11}$', help_text="Bunday telefon nomer mavjud")

    class Meta:
        model = Client
        fields = ['name', 'phone', 'district', 'region']

    def validate_phone(self, phone):
        if Client.objects.filter(phone=phone).exists():
            phone = self.phone
        else:
            raise ValidationError("Bu nomer ro'yxatdan o'tgan");
        return phone