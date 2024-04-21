from django.db import models

# Create your models here.
class ARM(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    time_update = models.DateTimeField(auto_now=True)
    domain = models.BooleanField(default=True)

    def __str__(self):
        return self.name    
