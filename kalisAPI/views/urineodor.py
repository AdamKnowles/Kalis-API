from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import UrineOdor
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class UrineOdorDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for UrineOdor dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = UrineOdor
        url = serializers.HyperlinkedIdentityField(
            view_name='urineodor',
            lookup_field='id'
        )
        fields = ('id', 'url', 'urine_odor',)

        depth = 1


class UrineOdorDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for UrineOdor

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            urine_odor = UrineOdor.objects.get(pk=pk)
            serializer = UrineOdorDropdownSerializer(urine_odor, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        urine_odor = UrineOdor.objects.all()
        
        serializer = UrineOdorDropdownSerializer(
            urine_odor, many=True, context={'request': request})
        return Response(serializer.data)

