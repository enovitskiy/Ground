from django import forms
from .models import Order,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class OrderService(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','phone','email','city','message','title','visitors','upload']
        widgets = {
            'name': forms.TextInput( attrs={'type': "text", 'class': "form-control", 'title': 'Call', 'required': "true", 'id': 'namecall', 'oninvalid': "this.setCustomValidity('Wow!')"}),
            'phone': forms.NumberInput(attrs={'type': "text", 'class': "form-control", 'title': 'Form', 'required': "true", 'id': 'formcall'}),
            'city': forms.TextInput(attrs={'type': "text", 'class': "form-control has-feedback", 'title': 'Form', 'required': "true",'id': 'formcall'}),
            'message': forms.TextInput( attrs={'type': "text", 'class': "form-control has-feedback", 'title': 'Form', 'required': "true",'id': 'formcall'}),
            'email': forms.EmailInput(attrs={'type': "email", 'class': "form-control", 'title':'Form','required':"true",'id':'formcall'}),
            'upload': forms.FileInput(attrs={'type':"file", 'name':"myfile",'multiple': True}),

        }
        labels = {
            'name': _('Name'),
            'phone': _('Phone 375123456789'),
            'email': _('email'),
            'city': _('city'),
            'message': _('message'),
            'upload': _('upload'),

        }





class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','phone','email','city','message','metka','title','visitors']
        widgets = {
            'name': forms.TextInput( attrs={'type': "text", 'class': "form-control", 'title': 'Call', 'required': "true", 'id': 'namecall','oninvalid': "this.setCustomValidity('Wow!')"}),
            'phone': forms.NumberInput(attrs={'type': "text", 'class': "form-control", 'title': 'Form', 'required': "true", 'id': 'formcall'}),
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
            'name': _('Name'),
            'phone': _('Phone 375123456789'),

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

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': "true"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control','required': "true"

        }
    ))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control' ,'required': "true"}))
    password2 = forms.CharField(label=_('Repeat password'), widget=forms.PasswordInput(attrs={'class': 'form-control' ,'required': "true"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(
                attrs={'type': "text", 'class': "form-control",'required': "true"}),
            'first_name': forms.TextInput(
                attrs={'type': "text", 'class': "form-control", 'required': "true"}),
            'email': forms.EmailInput(
                attrs={'type': "email", 'class': "form-control", 'required': "true"}),
        }



    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(_('Passwords don\'t match.'))
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'type': "text", 'class': "form-control",'required': "true"}),
            'last_name': forms.TextInput(
                attrs={'type': "text", 'class': "form-control", 'required': "true"}),
            'email': forms.EmailInput(
                attrs={'type': "email", 'class': "form-control", 'required': "true"}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        widgets = {
            'date_of_birth': forms.DateInput(format='%m/%d/%Y', attrs={
            'class': 'form-control datetimepicker','type':"text",}),
            'photo': forms.FileInput(attrs={'type': "file", 'name': "myfile", 'data-buttonText':"Your label here." ,'class':"btn btn-info btn-link btn-wd btn-lg", 'title':"your text",'placeholder':"Прикрепите файл"}),

        }
        labels = {
            'date_of_birth': _('date_of_birth'),
            'photo': _('photo'),


        }

