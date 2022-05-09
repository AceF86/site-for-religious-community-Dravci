from django.contrib import admin
from .models import Preaching, Day, History, News, Contacts


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date",
        "manage",
        "created",
        "updated",
    )
    ordering = (
        "name",
        "date",
    )
    search_fields = (
        "name",
        "date",
    )


@admin.register(Preaching)
class PreachingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "manage",
        "date",
        "created",
        "updated",
    )
    ordering = ("name",)
    search_fields = (
        "name",
        "manage",
    )


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "manage",
        "created",
        "updated",
    )
    ordering = ("name",)
    search_fields = (
        "name",
        "manage",
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "manage",
        "created",
        "updated",
    )
    ordering = ("name",)
    search_fields = (
        "name",
        "manage",
    )


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "phone",
        "created",
        "updated",
    )
    ordering = ("first_name",)
