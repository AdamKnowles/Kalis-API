from django.db import models
from .patient import Patient


class Notes(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=1000)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = ("note")
        verbose_name_plural = ("notes")