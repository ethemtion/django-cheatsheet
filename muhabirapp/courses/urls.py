from django.urls import path
from . import views

##Sıralama önemli.
urlpatterns = [
    path("", views.index),
    path("search", views.search),
    path("<slug:slug>", views.details, name='course_details'),
    # path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<slug:slug>', views.getCoursesByCategoryName, name='courses_by_category'),
    
]
