from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Day, History, Contacts, Preaching, News
from .forms import DayForm, NewsForm, PreachingForm, HistoryForm, ContactsForm, DayUpForm, PreachingUpForm
from django.contrib import messages
from datetime import date, timedelta
from django.db.models import Q


def index(request):
    contact = Contacts.objects.all()
    histor = History.objects.last()
    preaching = Preaching.objects.last()
    news = News.objects.last()
    event_list = Day.objects.filter(date=date.today())
    startdate = date.today()
    enddate = startdate + timedelta(6)
    event_week = Day.objects.filter(date__range=[startdate, enddate]).order_by("date")
    return render(
        request,
        "events/index.html",
        {
            "event_list": event_list,
            "histor": histor,
            "event_week": event_week,
            "contact": contact,
            "preaching": preaching,
            "news": news,
        },
    )


def admin_menu(request):
    p = Paginator(Day.objects.all().order_by("date"), 10)
    page = request.GET.get("page")
    event_week = p.get_page(page)
    nums = "a" * event_week.paginator.num_pages
    return render(
        request, "events/admin_menu.html", {"event_week": event_week, "nums": nums}
    )


def admin_news(request):
    p = Paginator(News.objects.all().order_by("id"), 10)
    page = request.GET.get("page")
    news = p.get_page(page)
    nums = "a" * news.paginator.num_pages
    return render(request, "events/admin_news.html", {"news": news, "nums": nums})


def admin_preaching(request):
    p = Paginator(Preaching.objects.all().order_by("id"), 10)
    page = request.GET.get("page")
    preaching = p.get_page(page)
    nums = "a" * preaching.paginator.num_pages
    return render(
        request, "events/admin_preaching.html", {"preaching": preaching, "nums": nums}
    )


def admin_history(request):
    p = Paginator(History.objects.all().order_by("id"), 10)
    page = request.GET.get("page")
    histor = p.get_page(page)
    nums = "a" * histor.paginator.num_pages
    return render(
        request, "events/admin_history.html", {"histor": histor, "nums": nums}
    )


def add_contacts(request):
    submitted = False
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_contacts?submitted=True")
    else:
        form = ContactsForm
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_contacts.html", {"form": form, "submitted": submitted}
    )


def add_days(request):
    submitted = False
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_days?submitted=True")
    else:
        form = DayForm
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_days.html", {"form": form, "submitted": submitted}
    )


def add_d(request):
    submitted = False
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_d?submitted=True")
    else:
        form = DayForm
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_d.html", {"form": form, "submitted": submitted}
    )


def add_news(request):
    submitted = False
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_news?submitted=True")
    else:
        form = NewsForm()
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_news.html", {"form": form, "submitted": submitted}
    )


def add_n(request):
    submitted = False
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_n?submitted=True")
    else:
        form = NewsForm()
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_n.html", {"form": form, "submitted": submitted}
    )


def add_preaching(request):
    submitted = False
    if request.method == "POST":
        form = PreachingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_preaching?submitted=True")
    else:
        form = PreachingForm()
        if "submitted" in request.GET:
            submitted = True

    return render(
        request,
        "events/main/add_preaching.html",
        {"form": form, "submitted": submitted},
    )


def add_p(request):
    submitted = False
    if request.method == "POST":
        form = PreachingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_p?submitted=True")
    else:
        form = PreachingForm()
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_p.html", {"form": form, "submitted": submitted}
    )


def add_history(request):
    submitted = False
    if request.method == "POST":
        form = HistoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_history?submitted=True")
    else:
        form = HistoryForm()
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_history.html", {"form": form, "submitted": submitted}
    )


def add_his(request):
    submitted = False
    if request.method == "POST":
        form = HistoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_his?submitted=True")
    else:
        form = HistoryForm()
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "events/main/add_his.html", {"form": form, "submitted": submitted}
    )


def update_news(request, news_id):
    newse = News.objects.get(pk=news_id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=newse)
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("admin-news")

    return render(
        request, "events/main/update_news.html", {"newse": newse, "form": form}
    )


def update_n(request, news_id):
    newse = News.objects.get(pk=news_id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=newse)
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("news")

    return render(request, "events/main/update_n.html", {"newse": newse, "form": form})


def update_history(request, history_id):
    histor = History.objects.get(pk=history_id)
    form = HistoryForm(request.POST or None, request.FILES or None, instance=histor)
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("admin-history")

    return render(
        request, "events/main/update_history.html", {"histor": histor, "form": form}
    )


def update_h(request, history_id):
    histor = History.objects.get(pk=history_id)
    form = HistoryForm(request.POST or None, request.FILES or None, instance=histor)
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("history")

    return render(
        request, "events/main/update_h.html", {"histor": histor, "form": form}
    )


def update_days(request, days_id):
    event_week = Day.objects.get(pk=days_id)
    form = DayUpForm(request.POST or None, instance=event_week)
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("admin-menu")

    return render(
        request,
        "events/main/update_days.html",
        {"event_week": event_week, "form": form},
    )


def update_d(request, days_id):
    event_week = Day.objects.get(pk=days_id)
    form = DayUpForm(request.POST or None, instance=event_week)
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("list_days")

    return render(
        request, "events/main/update_d.html", {"event_week": event_week, "form": form}
    )


def update_preaching(request, preaching_id):
    preaching = Preaching.objects.get(pk=preaching_id)
    form = PreachingUpForm(
        request.POST or None, request.FILES or None, instance=preaching
    )
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("admin-preaching")

    return render(
        request,
        "events/main/update_preaching.html",
        {"preaching": preaching, "form": form},
    )


def update_p(request, preaching_id):
    preaching = Preaching.objects.get(pk=preaching_id)
    form = PreachingUpForm(
        request.POST or None, request.FILES or None, instance=preaching
    )
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("preaching")

    return render(
        request, "events/main/update_p.html", {"preaching": preaching, "form": form}
    )


def update_contact(request, contact_id):
    contact = Contacts.objects.get(pk=contact_id)
    form = ContactsForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        messages.success(request, ("Зміни збережено"))
        return redirect("contact")

    return render(request, "events/main/update_contact.html", {"contact": contact, "form": form})


def delete_contact(request, contact_id):
    contact = Contacts.objects.get(pk=contact_id)
    contact.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("contact")


def delete_news(request, news_id):
    newse = News.objects.get(pk=news_id)
    newse.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("admin-news")


def delete_n(request, news_id):
    newse = News.objects.get(pk=news_id)
    newse.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("news")


def delete_history(request, history_id):
    histor = History.objects.get(pk=history_id)
    histor.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("admin-history")


def delete_his(request, history_id):
    histor = History.objects.get(pk=history_id)
    histor.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("history")


def delete_days(request, days_id):
    event_week = Day.objects.get(pk=days_id)
    event_week.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("admin-menu")


def delete_d(request, days_id):
    event_week = Day.objects.get(pk=days_id)
    event_week.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("list_days")


def delete_preaching(request, preaching_id):
    preaching = Preaching.objects.get(pk=preaching_id)
    preaching.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("admin-preaching")


def delete_p(request, preaching_id):
    preaching = Preaching.objects.get(pk=preaching_id)
    preaching.delete()
    messages.success(request, ("Успішно видалено"))
    return redirect("preaching")


def history(request):
    p = Paginator(History.objects.all().order_by("id"), 15)
    page = request.GET.get("page")
    histor = p.get_page(page)
    nums = "a" * histor.paginator.num_pages
    return render(request, "events/history.html", {"histor": histor, "nums": nums})


def preaching(request):
    p = Paginator(Preaching.objects.all().order_by("id"), 15)
    page = request.GET.get("page")
    preaching = p.get_page(page)
    nums = "a" * preaching.paginator.num_pages
    return render(
        request, "events/preaching.html", {"preaching": preaching, "nums": nums}
    )


def news(request):
    p = Paginator(News.objects.all().order_by("id"), 15)
    page = request.GET.get("page")
    news = p.get_page(page)
    nums = "a" * news.paginator.num_pages
    return render(request, "events/news.html", {"news": news, "nums": nums})


def list_days(request):
    p = Paginator(Day.objects.all().order_by("date"), 15)
    page = request.GET.get("page")
    event_week = p.get_page(page)
    nums = "a" * event_week.paginator.num_pages
    return render(
        request, "events/list_days.html", {"event_week": event_week, "nums": nums}
    )


def contact(request):
    contact = Contacts.objects.all()
    return render(request, "events/contact.html", {"contact": contact})


def show_history(request, history_id):
    histori = History.objects.get(pk=history_id)
    return render(request, "events/show/show_history.html", {"histori": histori})


def show_index_history(request, history_id):
    histori = History.objects.get(pk=history_id)
    return render(request, "events/show/show_index_history.html", {"histori": histori})


def show_news(request, news_id):
    newse = News.objects.get(pk=news_id)
    return render(request, "events/show/show_news.html", {"newse": newse})


def show_index_news(request, news_id):
    newse = News.objects.get(pk=news_id)
    return render(request, "events/show/show_index_news.html", {"newse": newse})


def show_admin_news(request, news_id):
    newse = News.objects.get(pk=news_id)
    return render(request, "events/show/show_admin_news.html", {"newse": newse})


def show_admin_preaching(request, preaching_id):
    preach = Preaching.objects.get(pk=preaching_id)
    return render(request, "events/show/show_admin_preaching.html", {"preach": preach})


def show_admin_histor(request, histor_id):
    histor = History.objects.get(pk=histor_id)
    return render(request, "events/show/show_admin_histor.html", {"histor": histor})


def show_preaching(request, preaching_id):
    preach = Preaching.objects.get(pk=preaching_id)
    return render(request, "events/show/show_preaching.html", {"preach": preach})


def show_index_preaching(request, preaching_id):
    preach = Preaching.objects.get(pk=preaching_id)
    return render(request, "events/show/show_index_preaching.html", {"preach": preach})


def show_search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        news = News.objects.filter(
            Q(name__contains=searched) | Q(description__contains=searched)
        )
        histor = History.objects.filter(
            Q(name__contains=searched) | Q(description__contains=searched)
        )
        preaching = Preaching.objects.filter(
            Q(name__contains=searched) | Q(description__contains=searched)
        )
        return render(
            request,
            "events/show/show_search.html",
            {
                "searched": searched,
                "news": news,
                "histor": histor,
                "preaching": preaching,
            },
        )
    else:
        searched = False
        return render(request, "events/show/show_search.html", {"searched": searched})


def show_search_news(request, news_id):
    newse = News.objects.get(pk=news_id)
    return render(request, "events/show/show_search_news.html", {"newse": newse})


def show_search_history(request, history_id):
    histori = History.objects.get(pk=history_id)
    return render(request, "events/show/show_search_history.html", {"histori": histori})


def show_search_preaching(request, preaching_id):
    preach = Preaching.objects.get(pk=preaching_id)
    return render(request, "events/show/show_search_preaching.html", {"preach": preach})


def show_days(request, days_id):
    event_week = Day.objects.get(pk=days_id)
    return render(request, "events/show/show_days.html", {"event_week": event_week})
