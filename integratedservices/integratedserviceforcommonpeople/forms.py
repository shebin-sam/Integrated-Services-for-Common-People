from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Service, SERVICE_TYPES
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'Entry', 'placeholder': 'YOUR NAME', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'Entry', 'placeholder': 'Enter your Email', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'textA', 'placeholder': 'Enter your suggestion or queries'}),
        }
class ServiceRegistrationForm(forms.ModelForm):
    service_type = forms.ChoiceField(choices=SERVICE_TYPES, widget=forms.RadioSelect)

    class Meta:
        model = Service
        fields = [
            'name', 'location', 'service_type', 'mobile_number', 'email',
            'whatsapp_number', 'website', 'address'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website and not website.startswith(('http://', 'https://')):
            website = 'http://' + website
        return website
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
