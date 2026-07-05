from django.db import models


class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    logo = models.ImageField(upload_to="company/")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    founded_year = models.IntegerField()

    def __str__(self):
        return self.name