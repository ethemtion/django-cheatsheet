from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

data = {
    "programlama": "Programlama kategorisine ait kurslar",
    "web-gelistirme": "Web gelistirme kategorisine ait kurslar",
    "mobil": "Mobil kategorisine ait kurslar",
}


def kurslar(request):
    return HttpResponse('Kurs Listesi')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfası')

def getCoursesByCategoryName(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
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
