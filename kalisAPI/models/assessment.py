from django.db import models
from .patient import Patient


class Assessment(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    mental_status = models.CharField(max_length=100)
    pupil_response = models.CharField(max_length=50)
    heart_sounds = models.CharField(max_length=50)
    breath_sounds = models.CharField(max_length=50)
    edema = models.CharField(max_length=50)
    oxygen_rate = models.IntegerField()
    bowel_sounds = models.CharField(max_length=50)
    npo = models.CharField(max_length=50)
    last_bowel_movement = models.DateField()
    urine_color = models.CharField(max_length=50)
    urine_odor = models.CharField(max_length=50)
    urine_amount = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = ("assessment")
        verbose_name_plural = ("assessments")

    