from django.db import models

# Create your models here.
class porflie(models.Model):
    porflie_img = models.ImageField(upload_to = 'porflie')
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    brithday = models.DateField()
    location = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name