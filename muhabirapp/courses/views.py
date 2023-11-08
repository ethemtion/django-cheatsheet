from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from .forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Course, Categories, UploadModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
import random
import os

# Create your views here.


def index(request):
    kurslar = Course.objects.filter(isActive=1, isHome=1)
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
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by(
            "date"
        )
        kategoriler = Categories.objects.all()
    else:
        return redirect("/kurslar")

    # paginator = Paginator(kurslar, 2)  # Sayfa başına2 kurs
    # page = request.GET.get("page", 1)
    # page_obj = paginator.page(page)

    return render(
        request,
        "courses/search.html",
        {"categories": kategoriler, "courses": kurslar},
    )


def isAdmin(user):
    return user.is_superuser


@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/kurslar")
    else:
        form = CourseCreateForm()

    return render(request, "courses/create-course.html", {"form": form})


@user_passes_test(isAdmin)
@login_required()  # settingsten login_url ayarlı user_passes_text ten kontrol?
def course_list(request):
    kurslar = Course.objects.all()

    return render(request, "courses/course-list.html", {"courses": kurslar})


@user_passes_test(isAdmin)
def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)
    return render(request, "courses/edit-course.html", {"form": form})


@login_required()
def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course-delete.html", {"course": course})


def upload_image(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", {"form": form})


def details(request, slug):
    try:
        course = Course.objects.get(slug=slug)
        print(course)
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
        "courses/list.html",
        {"categories": kategoriler, "page_obj": page_obj, "selectedSlug": slug},
    )
