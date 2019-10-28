from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import Patient
from kalisAPI.models import MyPatients
from .patient import PatientSerializer
from rest_framework.decorators import action

"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries for mypatients.
Methods: GET DELETE(id) POST"""


class MyPatientSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for mypatients
    Arguments:
        serializers
    """

    class Meta:
        model = MyPatients
        url = serializers.HyperlinkedIdentityField(
            view_name='mypatients',
            lookup_field='id'
        )
        fields = ('id', 'patient', 'user', 'user_id')

        depth = 1

        


class MyPatient(ViewSet):
    

    def retrieve(self, request, pk=None):
        """Handle GET requests for single patient
        Returns:
            Response -- JSON serialized mypatient instance
        """
        try:
            mypatients = MyPatients.objects.get(pk=pk)
            serializer = MyPatientSerializer(mypatients, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to mypatients resource
        Returns:
            Response -- JSON serialized list of orderproducts
        """
        mypatients = MyPatients.objects.all()

        serializer = MyPatientSerializer(
            mypatients, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def owner(self, request):

        mypatients = MyPatients.objects.all()
        current_user = User.objects.get(pk=request.user.pk)
        mypatients = MyPatients.objects.filter(user=current_user)

        serializer = MyPatientSerializer(
            mypatients, many=True, context={'request': request})
        return Response(serializer.data)