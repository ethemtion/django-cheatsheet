from datetime import date, datetime
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Course,Categories

# Create your views here.

data = {
    "programlama": "Programlama kategorisine ait kurslar",
    "web-gelistirme": "Web gelistirme kategorisine ait kurslar",
    "mobil": "Mobil kategorisine ait kurslar",
}

db = {
    "courses": [
        {
            "title": "JS Kursu",
            "description": "Javascript kurs açıklaması",
            "imageUrl": "1.jpg",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True
        },
        {
            "title": "Python Kursu",
            "description": "Python kurs açıklaması",
            "imageUrl": "2.jpg",
            "slug": "Python-kursu",
            "date": date(2022,9,10),
            "isActive": True

        },
        {
            "title": "Web Geliştirme Kursu",
            "description": "Web geliştirme kurs açıklaması",
            "imageUrl": "3.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2022,11,10),
            "isActive": True

        },
    ],
    "categories": [
        {"id": 1, "name": "Programlama", "slug":"programlama"}, 
        {"id": 2, "name": "web geliştirme", "slug":"web-gelistirme"}, 
        {"id": 3, "name": "mobil Uygulamalar", "slug":"mobil"}, 
        ]
}

def index(request):
    kurslar = Course.objects.filter(isActive = 1)
    kategoriler = Categories.objects.all()

    # for kurs in db["courses"]:
    #     if kurs["isActive"]:
    #         kurslar.append(kurs)


    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        "courses": kurslar
    })


def details(request, slug):
    try:
        course = Course.objects.get(slug=slug)
        context = {
            'course': course
        }

        return render(request, 'courses/details.html', context)
    except:
        raise Http404()


def getCoursesByCategoryName(request, slug):
   kurslar = Course.objects.filter(category__slug=slug, isActive=True)
   kategoriler = Categories.objects.all()

   return render(request, 'courses/index.html', {
       'categories': kategoriler,
       'courses': kurslar,
       'selectedSlug': slug
   })

