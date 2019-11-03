from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import BowelSounds
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class BowelSoundsDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for BowelSounds dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = BowelSounds
        url = serializers.HyperlinkedIdentityField(
            view_name='bowelsounds',
            lookup_field='id'
        )
        fields = ('id', 'url', 'bowel_sounds',)

        depth = 1


class BowelSoundsDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for BowelSounds

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            bowel_sounds = BowelSounds.objects.get(pk=pk)
            serializer = BowelSoundsDropdownSerializer(bowel_sounds, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        bowel_sounds = BowelSounds.objects.all()
        
        serializer = BowelSoundsDropdownSerializer(
            bowel_sounds, many=True, context={'request': request})
        return Response(serializer.data)

