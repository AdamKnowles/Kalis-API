from django.db import models



class BowelSounds(models.Model):
    
    bowel_sounds = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("bowel_sounds")
        verbose_name_plural = ("bowel_sounds")