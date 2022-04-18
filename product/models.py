from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'
    
    
