from django.db import models
from .patient import Patient
from .mentalstatus import MentalStatus
from .heartsounds import HeartSounds
from .breathsounds import BreathSounds
from .bowelsounds import BowelSounds
from .npo import Npo
from .pupilresponse import PupilResponse
from .edema import Edema
from .urinecolor import UrineColor
from .urineodor import UrineOdor
from .oxygenrate import OxygenRate


class Assessment(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    mental_status = models.ForeignKey(MentalStatus, on_delete=models.DO_NOTHING)
    pupil_response = models.ForeignKey(PupilResponse, on_delete=models.DO_NOTHING)
    heart_sounds = models.ForeignKey(HeartSounds, on_delete=models.DO_NOTHING)
    breath_sounds = models.ForeignKey(BreathSounds, on_delete=models.DO_NOTHING)
    edema = models.ForeignKey(Edema, on_delete=models.DO_NOTHING)
    oxygen_rate = models.ForeignKey(OxygenRate, on_delete=models.DO_NOTHING)
    bowel_sounds = models.ForeignKey(BowelSounds, on_delete=models.DO_NOTHING)
    npo = models.ForeignKey(Npo, on_delete=models.DO_NOTHING)
    last_bowel_movement = models.DateField()
    urine_color = models.ForeignKey(UrineColor, on_delete=models.DO_NOTHING)
    urine_odor = models.ForeignKey(UrineOdor, on_delete=models.DO_NOTHING)
    urine_amount = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = ("assessment")
        verbose_name_plural = ("assessments")

    