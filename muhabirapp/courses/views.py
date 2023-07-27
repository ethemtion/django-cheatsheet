from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def kurslar(request):
    return HttpResponse('Kurs Listesi')

def programlama(request):
    return HttpResponse('Programlama kurs Listesi')

def mobiluygulamalar(request):
    return HttpResponse('Mobil uygulama kurs Listesi')

def details(request):
    return HttpResponse('Kurs detay sayfası')
