from django.db import models



class PupilResponse(models.Model):
    
    pupil_response = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("pupil_response")
        verbose_name_plural = ("pupil_response")

    