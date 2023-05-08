from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.db import transaction
from .models import Users


class UpdateUser(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Users.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email has taken')
        return email

    def clean_password2(self):
        # check taht the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. include all the required
    fields, plus a repeated password
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirm', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        users = super(UserAdminCreationForm, self).save(commit=False)
        users.set_password(self.cleaned_data["password1"])
        if commit:
            users.save()
        return users


class UserAdminChangeForm(forms.ModelForm):
    """
    A Form for updating users. Include all the fields on the user,
    but replaces the password field with admin's password hash display
    field
    """
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = Users
        fields = ('email', 'password', 'is_active')

    def clean_password(self):

        # Regardless of what the user provides, return the initial value
        # This is done here, rather than on the field, because the
        # field does not have acces to the initial value
        return self.initial['password']
