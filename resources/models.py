from django.db import models

# Create your models here.
class Resource(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField()
 url = models.URLField(max_length=500, null=True, blank=True)
 published_date = models.DateTimeField(auto_now_add=True)

 def __str__(self):
     return self.title