from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import HeartSounds
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class HeartSoundsDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for heartsounds dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = HeartSounds
        url = serializers.HyperlinkedIdentityField(
            view_name='heartsounds',
            lookup_field='id'
        )
        fields = ('id', 'url', 'heart_sounds',)

        depth = 1


class HeartSoundsDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for heartsounds

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            heart_sounds = HeartSounds.objects.get(pk=pk)
            serializer = HeartSoundsDropdownSerializer(heart_sounds, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        heart_sounds = HeartSounds.objects.all()
        
        serializer = HeartSoundsDropdownSerializer(
            heart_sounds, many=True, context={'request': request})
        return Response(serializer.data)

