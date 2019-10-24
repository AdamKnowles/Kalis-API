from django.db import models
from django.contrib.auth.models import User
from .patient import Patient

class MyPatients(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("mypatient")
        verbose_name_plural = ("mypatients")

   