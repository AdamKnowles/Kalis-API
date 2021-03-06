from django.db import models
from .patientgender import PatientGender
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE


class Patient(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.ForeignKey(PatientGender, on_delete=models.DO_NOTHING)
    diagnosis = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")

    def __str__(self):
        return self.last_name

