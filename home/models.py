from django.db import models


class People(models.Model):
    # Name of the person
    name = models.CharField(max_length=50)
    # Name of the image file, refer a default file when no image
    # TODO: consider replace this with FilePathField
    image = models.CharField(max_length=200)
    # Email address of the person
    mail = models.CharField(max_length=100, null=True, blank=True)
    # Introduction
    about = models.CharField(max_length=1000, null=True, blank=True)
    # Google scholar link, cloud be null
    google_scholar = models.CharField(max_length=200, null=True, blank=True)
    # Position of the person
    POSITION_CHOICES = [
        ("prof", "professor"),
        ("phd", "phd"),
        ("ms", "master"),
        ("ug", "undergraduate"),
        ("al.phd", "alumni phd"),
        ("al.ms", "alumni master"),
        ("al.ug", "alumni undergraduate"),
    ]
    position = models.CharField(max_length=8, choices=POSITION_CHOICES)

    class Meta:
        # This is an abstract class for all people
        abstract = True
        # Sorted by name in ascending order
        ordering = ["name"]

    def __str__(self):
        return self.name


'''
    Student class and Professor class are identical now,
    but may be different in future.
'''


class Student(People):
    pass


class Professor(People):
    pass


class Paper(models.Model):
    name = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    link = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    TYPE_CHOICES = [
        ("cwp", "conference and workshop proceedings"),
        ("prp", "peer reviewed journal papers"),
        ("sp", "selected papers"),
    ]
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    leader = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    description = models.CharField(max_length=100)
    date = models.DateField()
    link = models.CharField(max_length=200)
    # Higher number means higher importance, should be within 1-5
    importance = models.IntegerField(default=3)

    class Meta:
        # Sorted first by importance in descending order
        # then by datetime in descending order
        ordering = ["-importance", "-date"]

    def __str__(self):
        return self.description
