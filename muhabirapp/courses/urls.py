from django.urls import path
from . import views

##Sıralama önemli.
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create-course", views.create_course, name="create_course"),
    path("course-list", views.course_list, name="course_list"),
    path("course-edit/<int:id>", views.course_edit, name="course_edit"),
    path("course-delete/<int:id>", views.course_delete, name="course_delete"),
    path("upload", views.upload_image, name="upload_image"),
    path("<slug:slug>", views.details, name="course_details"),
    # path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path(
        "kategori/<slug:slug>",
        views.getCoursesByCategoryName,
        name="courses_by_category",
    ),
]
