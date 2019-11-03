from django.db import models



class UrineColor(models.Model):
    
    urine_color = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("urine_color")
        verbose_name_plural = ("urine_color")

    