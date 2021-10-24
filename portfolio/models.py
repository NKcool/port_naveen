from django.db import models

class project(models.Model):
    tital = models.CharField(max_length = 100)
    discription = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.tital
