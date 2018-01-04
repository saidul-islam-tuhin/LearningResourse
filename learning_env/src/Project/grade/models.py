"""from django.db import models

# Create your models here.
class Subject(models.Model):
    sub_name = models.CharField(max_length=128,primary_key=True)
    credit=models.IntegerField(max_length=10)


    def __str__(self):              # __unicode__ on Python 2
        return self.sub_name


class Student(models.Model):
    std_id=models.IntegerField(max_length=50,primary_key=True)
    std_name = models.CharField(max_length=128)
    batch = models.CharField(max_length=10)
    members = models.ManyToManyField(Subject, through='Point')
    def __str__(self):              # __unicode__ on Python 2
        return self.std_name


class Point(models.Model):
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sub_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(max_length=64)

    def __str__(self):              # __unicode__ on Python 2

        return self.std_id , self.sub_name"""
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.details         #from grade.models import Blog,Author,Entry,EntryDetail
