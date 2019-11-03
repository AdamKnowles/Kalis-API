from django.db import models



class HeartSounds(models.Model):
    
    heart_sounds = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("heart_sounds")
        verbose_name_plural = ("heart_sounds")