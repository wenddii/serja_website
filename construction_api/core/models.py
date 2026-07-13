from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    logo = models.ImageField(upload_to="company/")
    hero_image = models.ImageField(upload_to="company/", blank=True, null=True)

    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    founded_year = models.PositiveIntegerField()

    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)

    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    testimonial = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name