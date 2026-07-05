from django.db import models
from django.utils.text import slugify


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("planned", "Planned"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, related_name="projects")

    description = models.TextField()

    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ongoing")

    cover_image = models.ImageField(upload_to="projects/covers/")

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/images/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"