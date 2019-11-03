from django.db import models



class OxygenRate(models.Model):
    
    oxygen_rate = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("oxygen_rate")
        verbose_name_plural = ("oxygen_rate")
