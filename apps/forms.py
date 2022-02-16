from django import forms
from django.forms import ModelForm
from apps.models import MyUser

class UserForm(ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password_confirmation',)

    def clean(self):
        data = self.cleaned_data
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Passwords do not match!')
        return data
