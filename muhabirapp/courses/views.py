from datetime import date, datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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
    kurslar = [course for course in db["courses"] if course["isActive"]]
    kategoriler = db["categories"]

    # for kurs in db["courses"]:
    #     if kurs["isActive"]:
    #         kurslar.append(kurs)


    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        "courses": kurslar
    })

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfası')



def getCoursesByCategoryName(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/kurslar.html', {
            'category': category_name,
            "category_text": category_text
        })
    except:
        return HttpResponseNotFound("Yanlış kategori seçimi")
        



def getCoursesByCategoryId(request, category_id):
    # return HttpResponse(category_id)

    category_list = list(data.keys())
    try:
        category_name = category_list[category_id-1]

        redirect_url = reverse('courses_by_category', args=[category_name])
        return redirect(redirect_url)
    except:
        return HttpResponseNotFound("S")
