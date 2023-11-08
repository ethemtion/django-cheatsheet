from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, default="", null=False, unique=True, db_index=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default="")
    description = RichTextField()
    image = models.ImageField(upload_to="images", default="")
    date = models.DateField(auto_now=True)  # auto_now olabilirdi
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(
        default="", blank=True, editable=True, null=False, unique=True, db_index=True
    )
    # category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1, related_name="kurslar")
    categories = models.ManyToManyField(Categories)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.title} {self.date}"


# c1.course_set.all() categorye ait kurslar (related_name kurslar -> c1.kurslar.all())


class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")
