from django.db import models



class PatientGender(models.Model):
    
    sex = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("sex")
        verbose_name_plural = ("sex")

    