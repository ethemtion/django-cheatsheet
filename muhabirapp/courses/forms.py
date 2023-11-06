from django import forms

from .models import Course, Categories


# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Kurs Başlığı",
#         error_messages={"required": "Kurs başlığı girilmeli"},
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#     )
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={"class": "form-control"})
#     )
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class": "form-control"}))


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "slug", "image")  # __all__
        labels = {
            "title": "Kurs başlığı",
            "description": "Kurs açıklaması",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "title": {
                "required": "Kurs başlığını girin.",
                "max_length": "Max 50 karakter",
            },
            "description": {"required": "Kurs açıklaması girilmelidir."},
        }


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "slug",
            "categories",
            "isActive",
            "image",
        )  # __all__
        labels = {
            "title": "Kurs başlığı",
            "description": "Kurs açıklaması",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        error_messages = {
            "title": {
                "required": "Kurs başlığını girin.",
                "max_length": "Max 50 karakter",
            },
            "description": {"required": "Kurs açıklaması girilmelidir."},
        }


class UploadForm(forms.Form):
    image = forms.ImageField()
