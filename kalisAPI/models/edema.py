from django.db import models



class Edema(models.Model):
    
    edema = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("edema")
        verbose_name_plural = ("edema")