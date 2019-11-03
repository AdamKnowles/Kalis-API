from django.db import models



class BreathSounds(models.Model):
    
    breath_sounds = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("breath_sounds")
        verbose_name_plural = ("breath_sounds")