from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from kalisAPI.views import register_user, login_user
from kalisAPI.models import *
from kalisAPI.views import UserViewSet
from kalisAPI.views import Patients
from kalisAPI.views import VitalSign
from kalisAPI.views import Assessments
from kalisAPI.views import MyPatient
from kalisAPI.views import MentalStatusDropdown
from kalisAPI.views import HeartSoundsDropdown
from kalisAPI.views import BreathSoundsDropdown
from kalisAPI.views import BowelSoundsDropdown
from kalisAPI.views import NpoDropdown
from kalisAPI.views import PupilResponseDropdown
from kalisAPI.views import EdemaDropdown
from kalisAPI.views import UrineColorDropdown
from kalisAPI.views import UrineOdorDropdown
from kalisAPI.views import OxygenRateDropdown
from kalisAPI.views import PatientGenderDropdown









router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, 'user')
router.register(r'patients', Patients, 'patient')
router.register(r'vitalsigns', VitalSign, 'vitalsign')
router.register(r'assessments', Assessments, 'assessment')
router.register(r'mypatients', MyPatient, 'mypatient')
router.register(r'mentalstatus', MentalStatusDropdown , 'mentalstatus')
router.register(r'heartsounds', HeartSoundsDropdown , 'heartsounds')
router.register(r'breathsounds', BreathSoundsDropdown , 'breathsounds')
router.register(r'bowelsounds', BowelSoundsDropdown , 'bowelsounds')
router.register(r'npo', NpoDropdown , 'npo')
router.register(r'pupilresponse', PupilResponseDropdown , 'pupilresponse')
router.register(r'edema', EdemaDropdown , 'edema')
router.register(r'urinecolor', UrineColorDropdown , 'urinecolor')
router.register(r'urineodor', UrineOdorDropdown , 'urineodor')
router.register(r'oxygenrate', OxygenRateDropdown , 'oxygenrate')
router.register(r'patientgender', PatientGenderDropdown , 'patientgender')



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    
]