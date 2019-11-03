from django.db import models



class MentalStatus(models.Model):
    
    mental_status = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("mental_status")
        verbose_name_plural = ("mental_status")

    