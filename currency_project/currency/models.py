from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=100) #Название валюты
    rate = models.DecimalField(max_digits=10, 
                               decimal_places=2,
                               null=True, blank=True) #Курс
    logo_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name