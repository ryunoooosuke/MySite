from django.db import models
from django.utils import timezone
# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=200, default="")
    sub_title = models.CharField(max_length=200, blank=True, default="")
    main_text = models.TextField(max_length=1000, blank=True, default="")
    main_text_english = models.TextField(max_length=1000, blank=True, default="")
    contents_type = models.CharField(max_length=20, default="SITE")
    date_created = models.DateTimeField(default=timezone.now)
    date_changed = models.DateTimeField(default=timezone.now)
    avator = models.ImageField(verbose_name='avator', upload_to='myprofile/', blank=True, default="")

    def __str__(self):
        return self.title


class Skill(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="related_content")
    name = models.CharField(max_length=200, default="")
    rank = models.IntegerField(default=0)
    type = models.CharField(max_length=20, default="")
    date_created = models.DateTimeField(default=timezone.now)
    date_changed = models.DateTimeField(default=timezone.now)


class Work(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="work_content")
    name = models.CharField(max_length=200, default="")
    top_image = models.ImageField(verbose_name='top_image', upload_to='myprofile/')
    date_created = models.DateTimeField(default=timezone.now)
    date_changed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class SubWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="sub_work_content")
    main_text = models.TextField(max_length=1000, blank=True, default="")
    sub_text = models.TextField(max_length=1000, blank=True, default="")
    sub_image_1 = models.ImageField(verbose_name='sub_image_1', upload_to='myprofile/', blank=True, default="")
    sub_image_2 = models.ImageField(verbose_name='sub_image_1', upload_to='myprofile/', blank=True, default="")
    sub_image_3 = models.ImageField(verbose_name='sub_image_1', upload_to='myprofile/', blank=True, default="")
    sub_image_4 = models.ImageField(verbose_name='sub_image_1', upload_to='myprofile/', blank=True, default="")
    sub_image_5 = models.ImageField(verbose_name='sub_image_1', upload_to='myprofile/', blank=True, default="")
    link = models.CharField(max_length=500, blank=True, default="")
    date_created = models.DateTimeField(default=timezone.now)
    date_changed = models.DateTimeField(default=timezone.now)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
