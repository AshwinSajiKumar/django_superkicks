from django.db import models

class product(models.Model):
    img=models.ImageField(upload_to="picture")
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    
