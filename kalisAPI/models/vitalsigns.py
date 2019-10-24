from django.db import models
from .patient import Patient


class VitalSigns(models.Model):
    time = models.DateField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    heart_rate = models.IntegerField()
    blood_pressure = models.CharField(max_length=50)
    respiration_rate = models.IntegerField()
    oxygen_saturation = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = ("vitalsign")
        verbose_name_plural = ("vitalsigns")

    