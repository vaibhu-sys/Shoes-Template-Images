from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=500)
    pdes=models.TextField(max_length=600)
    prize=models.FloatField()
    image=models.ImageField(upload_to="images/")



    def __str__(self):
        return self.pname