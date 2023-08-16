from django.db import models
from django.utils.text import slugify


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, blank=True, editable=False, null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, kwargs)


    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date =  models.DateField(auto_now=True)#auto_now olabilirdi
    isActive = models.BooleanField()
    slug = models.SlugField(default="", blank=True, editable=False, null=False, unique=True, db_index=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1, related_name="kurslar")


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)


    def __str__(self):
        return f"{self.title} {self.date}"
    

#c1.course_set.all() categorye ait kurslar (related_name kurslar -> c1.kurslar.all())