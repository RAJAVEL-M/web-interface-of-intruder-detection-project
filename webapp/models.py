from django.db import models

# Create your models here.
class detail(models.Model):
    time = models.CharField(max_length=100)
    #frame = jsonfield(upload_to='media/')
    frame = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.time
