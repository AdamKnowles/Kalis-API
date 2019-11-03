from django.db import models
from .patient import Patient
from .mentalstatus import MentalStatus
from .heartsounds import HeartSounds
from .breathsounds import BreathSounds
from .bowelsounds import BowelSounds
from .npo import Npo


class Assessment(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    mental_status = models.ForeignKey(MentalStatus, on_delete=models.DO_NOTHING)
    pupil_response = models.CharField(max_length=50)
    heart_sounds = models.ForeignKey(HeartSounds, on_delete=models.DO_NOTHING)
    breath_sounds = models.ForeignKey(BreathSounds, on_delete=models.DO_NOTHING)
    edema = models.CharField(max_length=50)
    oxygen_rate = models.IntegerField()
    bowel_sounds = models.ForeignKey(BowelSounds, on_delete=models.DO_NOTHING)
    npo = models.ForeignKey(Npo, on_delete=models.DO_NOTHING)
    last_bowel_movement = models.DateField()
    urine_color = models.CharField(max_length=50)
    urine_odor = models.CharField(max_length=50)
    urine_amount = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = ("assessment")
        verbose_name_plural = ("assessments")

    