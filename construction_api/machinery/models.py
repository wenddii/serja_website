from django.db import models


class Machinery(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="machinery/")
    description = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
