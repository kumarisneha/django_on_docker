from django import forms
from django.core.validators import RegexValidator
from .models import Address
from django.forms import ModelForm, Textarea,TextInput
from django.core.exceptions import ValidationError

class AddressBookForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['id','user','email_id','address','phone_number']
        widgets = {
            'user': TextInput(attrs={'class':'form-control','name':'user','placeholder':'User Name'}),
            'email_id': TextInput(attrs={'class':'form-control form-control-solid placeholder-no-fix','placeholder':'Email'}),
            'address': TextInput(attrs={'class':'form-control form-control-solid placeholder-no-fix','placeholder':'Address'}),
            'phone_number': TextInput(attrs={'class':'form-control form-control-solid placeholder-no-fix','placeholder':'Phone number'}),
        
        }

    def clean_phone_number(self):
        phone_num=self.cleaned_data.get('phone_number', None)
        try:
            int(phone_num)
        except (ValueError, TypeError):
            raise ValidationError("Please enter a valid phone number")
        return phone_num

    def clean_email_id(self):
        data = self.cleaned_data['email_id']
        domain = data.split('@')[1]
        domain_list = ["gmail.com", "yahoo.com", "hotmail.com",]
        if domain not in domain_list:
            raise ValidationError("Please enter an Email Address with a valid domain")
        return data
