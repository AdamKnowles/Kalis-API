from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import OxygenRate
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class OxygenRateDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for OxygenRate dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = OxygenRate
        url = serializers.HyperlinkedIdentityField(
            view_name='oxygenrate',
            lookup_field='id'
        )
        fields = ('id', 'url', 'oxygen_rate',)

        depth = 1


class OxygenRateDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for OxygenRate

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            oxygen_rate = OxygenRate.objects.get(pk=pk)
            serializer = OxygenRateDropdownSerializer(oxygen_rate, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        oxygen_rate = OxygenRate.objects.all()
        
        serializer = OxygenRateDropdownSerializer(
            oxygen_rate, many=True, context={'request': request})
        return Response(serializer.data)

