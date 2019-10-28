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

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, 'user')
router.register(r'patients', Patients, 'patient')
router.register(r'vitalsigns', VitalSign, 'vitalsign')
router.register(r'assessments', Assessments, 'assessment')
router.register(r'mypatients', MyPatient, 'mypatient')



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    
]