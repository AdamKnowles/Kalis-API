from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import PatientGender
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class PatientGenderDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for PatientGender dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = PatientGender
        url = serializers.HyperlinkedIdentityField(
            view_name='patientgender',
            lookup_field='id'
        )
        fields = ('id', 'url', 'sex',)

        depth = 1


class PatientGenderDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for PatientGender

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            sex = PatientGender.objects.get(pk=pk)
            serializer = PatientGenderDropdownSerializer(sex, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        sex = PatientGender.objects.all()
        
        serializer = PatientGenderDropdownSerializer(
            sex, many=True, context={'request': request})
        return Response(serializer.data)