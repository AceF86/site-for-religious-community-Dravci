from django import forms
from django.forms import ModelForm
from .models import Preaching, Day, History, News, Contacts


class DayForm(ModelForm):
    class Meta:
        model = Day
        fields = ("name", "date", "manage", "list")

        labels = {
            "name": "",
            "date": "Дата події",
            "manage": "Модератор",
            "list": "Список",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            'date': forms.DateInput(attrs={"class": "form-control",'type': 'date'}),
            "manage": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "list": forms.Textarea(attrs={"class": "form-control"}),
        }


class DayUpForm(ModelForm):
    class Meta:
        model = Day
        fields = ("name", "date", "manage", "list")

        labels = {
            "name": "",
            "date": "Дата події",
            "manage": "Модератор",
            "list": "Список",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            'date': forms.SelectDateWidget(attrs={'class':'datepicker form-control', 'placeholder':'Select a date'}),
            "manage": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "list": forms.Textarea(attrs={"class": "form-control"}),
        }


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ("name", "photo", "manage", "description")

        labels = {
            "name": "",
            "photo": "Фото",
            "manage": "Модератор",
            "description": "Опис",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            "manage": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class PreachingForm(ModelForm):
    class Meta:
        model = Preaching
        fields = ("name", "date", "photo", "manage", "description")

        labels = {
            "name": "",
            "date": "Дата події",
            "photo": "Фото",
            "manage": "Модератор",
            "description": "Опис",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "manage": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class PreachingUpForm(ModelForm):
    class Meta:
        model = Preaching
        fields = ("name", "date", "photo", "manage", "description")

        labels = {
            "name": "",
            "date": "Дата події",
            "photo": "Фото",
            "manage": "Модератор",
            "description": "Опис",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            'date': forms.SelectDateWidget(attrs={'class':'datepicker form-control', 'placeholder':'Select a date'}),
            "manage": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ("name", "photo", "manage", "description")

        labels = {
            "name": "",
            "photo": "Фото",
            "manage": "Модератор",
            "description": "Опис",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            "manage": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ("first_name", "phone", "facebook",)

        labels = {
            "first_name": "Ім'я, Прізвище",
            "phone": "мобільні телефон",
            "facebook": "facebook",
        }

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            "phone": forms.NumberInput(attrs={"class": "form-control form-label", "for": "typePhone"}),

        }
