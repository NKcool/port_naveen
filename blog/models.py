from django.db import models



class blog(models.Model):
    blog_tital = models.CharField(max_length = 250)
    discription = models.TextField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.blog_tital
