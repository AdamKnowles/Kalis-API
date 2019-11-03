from django.db import models



class UrineOdor(models.Model):
    
    urine_odor = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("urine_odor")
        verbose_name_plural = ("urine_odor")

    