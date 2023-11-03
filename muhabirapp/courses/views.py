from datetime import date, datetime
from django.shortcuts import redirect, render
from django.http import (
    Http404,
)

from .models import Course, Categories
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Categories.objects.all()

    # for kurs in db["courses"]:
    #     if kurs["isActive"]:
    #         kurslar.append(kurs)

    return render(
        request, "courses/index.html", {"categories": kategoriler, "courses": kurslar}
    )


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains = q ).order_by(
            "date"
        )
        kategoriler = Categories.objects.all()
    else:
        return redirect("/kurslar")
    
    paginator = Paginator(kurslar, 2)  # Sayfa başına2 kurs
    page = request.GET.get("page", 1)
    page_obj = paginator.page(page)

    return render(
        request,
        "courses/list.html",
        {"categories": kategoriler, "page_obj": page_obj},
    )


def details(request, slug):
    try:
        course = Course.objects.get(slug=slug)
        context = {"course": course}

        return render(request, "courses/details.html", context)
    except:
        raise Http404()


def getCoursesByCategoryName(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by(
        "date"
    )
    kategoriler = Categories.objects.all()

    paginator = Paginator(kurslar, 2)  # Sayfa başına2 kurs
    page = request.GET.get("page", 1)
    page_obj = paginator.page(page)

    return render(
        request,
        "courses/index.html",
        {"categories": kategoriler, "page_obj": page_obj, "selectedSlug": slug},
    )
