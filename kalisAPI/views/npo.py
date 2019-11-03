from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import Npo
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class NpoDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Npo dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = Npo
        url = serializers.HyperlinkedIdentityField(
            view_name='npo',
            lookup_field='id'
        )
        fields = ('id', 'url', 'npo',)

        depth = 1


class NpoDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for Npo

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            npo = Npo.objects.get(pk=pk)
            serializer = NpoDropdownSerializer(npo, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        npo = Npo.objects.all()
        
        serializer = NpoDropdownSerializer(
            npo, many=True, context={'request': request})
        return Response(serializer.data)

