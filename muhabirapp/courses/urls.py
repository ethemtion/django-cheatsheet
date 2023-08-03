from django.urls import path
from . import views

##Sıralama önemli.
urlpatterns = [
    path("", views.index),
    path("<kurs_adi>", views.details),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<str:category_name>', views.getCoursesByCategoryName, name='courses_by_category'),
    
]
