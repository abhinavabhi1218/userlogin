from django import forms
from django.forms import fields, widgets
from .models import Products
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=(forms.PasswordInput(attrs={'class':'form-control'})))
    password2 = forms.CharField(label='Confirm Password(again)', widget=(forms.PasswordInput(attrs={'class':'form-control'})))

    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=(forms.TextInput()))
    price = forms.FloatField()
    discount_price = forms.FloatField()
    rating = forms.FloatField()
    category = forms.CharField(widget=(forms.TextInput()))
    description = forms.CharField(widget=(forms.Textarea(attrs={'style':'height:200px;width:500px'})))
    image = forms.CharField(widget=(forms.URLInput()))

    class Meta:
        model = Products    
        fields= '__all__'
        labels = {'title':'Tile', 'price':'Price', 'discount_price':'Discount_Price', 'category':'Category',
        'description':'Description', 'image': 'Image_url', 'rating': 'Rating'}
        # attrs={'title':{'class':'form-control'},'price':{'class':'form-control'},'discount_price':{'class':'form-control'},
        # 'category':{'class':'form-control'},'description':{'class':'form-control'},'image':{'class':'form-control'}}