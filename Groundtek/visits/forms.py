from django import forms
from .models import Order,Profile
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class OrderService(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email','city','message']
        widgets = {
            'city': forms.TextInput(attrs={'type': "text", 'class': "form-control has-feedback", 'title': 'Form', 'required': "true",'id': 'formcall'}),
            'message': forms.TextInput( attrs={'type': "text", 'class': "form-control has-feedback", 'title': 'Form', 'required': "true",'id': 'formcall'}),
            'email': forms.EmailInput(attrs={'type': "email", 'class': "form-control", 'title':'Form','required':"true",'id':'formcall'}),
        }
        labels = {
            'email': _('email'),
            'city': _('city'),
            'message': _('message'),

        }





class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email','city','message','metka']
        widgets = {
            'city': forms.TextInput(attrs={'type': "text", 'class': "form-control has-feedback", 'title': 'Form', 'required': "true",'id': 'formcall'}),
            'message': forms.TextInput( attrs={'type': "text", 'class': "form-control has-feedback", 'title': 'Form', 'required': "true",'id': 'formcall'}),
            'email': forms.EmailInput(attrs={'type': "email", 'class': "form-control", 'title':'Form','required':"true",'id':'formcall'}),
            'metka': forms.Select(attrs={'type': "text", 'class':"form-control", 'title':'Form','required':"true",'id':'formcall'}),
        }
        labels = {
            'email': _('email'),
            'city': _('city'),
            'message': _('message'),
            'metka': _('metka'),

        }



class OrderCall(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','phone','title','visitors']
        widgets = {
            'name': forms.TextInput(attrs={'type':"text", 'class':"form-control", 'title':'Call','required':"true",'id':'namecall','oninvalid':"this.setCustomValidity('Wow!')"}),
            'phone': forms.NumberInput(attrs={'type': "text", 'class': "form-control",'title': 'Form', 'required': "true", 'id': 'formcall'}),
        }
        labels = {
            'name': _('Name'),
            'phone': _('Phone 375123456789'),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')