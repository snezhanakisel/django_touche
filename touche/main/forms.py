from django.forms import ModelForm, TextInput, Textarea
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name':TextInput(attrs={
                'class':'form-control',
                'id': 'name',
                'placeholder':'Name'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'name@example.com'
        }),
           'message': Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Message'

            })
        }
