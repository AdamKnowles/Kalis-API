from django.db import models



class Npo(models.Model):
    
    npo = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("npo")
        verbose_name_plural = ("npo")

    