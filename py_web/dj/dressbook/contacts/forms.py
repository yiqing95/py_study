__author__ = 'yiqing'

from contacts.models import Contact
from django.core.exceptions import  ValidationError

from django import forms

# TODO 这个类里面的clean方法有bug！
class ContactForm(forms.ModelForm):

    confirm_email = forms.EmailField("Confirm email",
                                     required=True
    )

    class Meta:
        model = Contact

    def clean(self):
        if(self.cleaned_data.get('email') !=
        self.cleaned_data.get('confirm_email')
        ):
            raise ValidationError('Email addr must match')

        return self.cleaned_data