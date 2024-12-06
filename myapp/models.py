from django.db import models

class Modelos_nexu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    average_price = models.IntegerField()
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
