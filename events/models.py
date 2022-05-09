from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Preaching(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField("заголовок", max_length=250, blank=True)
    date = models.DateField("дату публікування", null=True)
    photo = models.ImageField("фото", blank=True, null=True, upload_to="images_p/")
    manage = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = RichTextField(blank=True, null=True)
    created = models.DateTimeField("створено", auto_now_add=True)
    updated = models.DateTimeField("обновлено", auto_now=True)

    def __str__(self):
        return self.name


class Day(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField("заголовок", max_length=500, blank=True)
    date = models.DateField("дату публікування", null=True)
    manage = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    list = RichTextField("Список", blank=True, null=True)
    created = models.DateTimeField("створено", auto_now_add=True)
    updated = models.DateTimeField("обновлено", auto_now=True)

    def __str__(self):
        return self.name


class History(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField("заголовок", max_length=500, blank=True)
    photo = models.ImageField(blank=True, null=True, upload_to="images_h/")
    manage = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = RichTextField(blank=True, null=True)
    created = models.DateTimeField("створено", auto_now_add=True)
    updated = models.DateTimeField("обновлено", auto_now=True)

    def __str__(self):
        return self.name


class News(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField("заголовок", max_length=500)
    photo = models.ImageField(blank=True, null=True, upload_to="images_n/")
    manage = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = RichTextField(blank=True, null=True)
    created = models.DateTimeField("створено", auto_now_add=True)
    updated = models.DateTimeField("обновлено", auto_now=True)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField("Ім'я, Прізвище", max_length=200, blank=True)
    phone = models.IntegerField("мобільні телефон", blank=True)
    facebook = models.URLField("facebook", blank=True)
    email = models.EmailField("e-mail", blank=True)
    manage = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField("створено", auto_now_add=True)
    updated = models.DateTimeField("обновлено", auto_now=True)

    def __str__(self):
        return self.first_name
