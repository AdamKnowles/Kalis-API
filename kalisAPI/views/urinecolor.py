from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import UrineColor
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class UrineColorDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for UrineColor dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = UrineColor
        url = serializers.HyperlinkedIdentityField(
            view_name='urinecolor',
            lookup_field='id'
        )
        fields = ('id', 'url', 'urine_color',)

        depth = 1


class UrineColorDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for UrineColor

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            urine_color = UrineColor.objects.get(pk=pk)
            serializer = UrineColorDropdownSerializer(urine_color, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        urine_color = UrineColor.objects.all()
        
        serializer = UrineColorDropdownSerializer(
            urine_color, many=True, context={'request': request})
        return Response(serializer.data)

