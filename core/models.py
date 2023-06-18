from django.db import models
from django.utils import timezone


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


class PersonalProjects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name


class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    begindate = models.DateField(default=timezone.now)
    enddate = models.DateField(default=timezone.now)
    description = models.TextField(null=True)
    tecnologies = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill name")
    description = models.TextField(verbose_name="Skill description")
    skill_level = models.FloatField()

    def __str__(self):
        return self.name


class Tool(models.Model):
    level_choices = [
            ("B", "Basic"),
            ("I", "Intermediate"),
            ("A", "Advanced"),
            ]
    """Model definition for Tool."""
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    level = models.CharField(max_length=10, choices=level_choices)

    class Meta:
        """Meta definition for Tool."""

        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def __str__(self):
        return self.name


class Course(models.Model):
    """Model definition for Course."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    institution = models.CharField(max_length=50)
    certificate = models.ImageField(upload_to="course")

    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self, arg):
        return self.name
