from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django.forms import ValidationError, widgets
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["password"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password2"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["username"].widget = widgets.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["email"].widget = widgets.EmailInput(
            attrs={"class": "form-control"}
        )
        self.fields["email"].required = True

    def clean_password1(self):
        # super().clean_password2() temeldeki de çalışsın diye
        pass

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error(field="email", error="Bu kullanıcı adı kullanılıyor.")


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["new_password2"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["old_password"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )

    def clean_password1(self):
        # super().clean_password2() temeldeki de çalışsın diye
        pass

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error(field="email", error="Bu kullanıcı adı kullanılıyor.")
