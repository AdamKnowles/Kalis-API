from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import Edema
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class EdemaDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Edema dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = Edema
        url = serializers.HyperlinkedIdentityField(
            view_name='edema',
            lookup_field='id'
        )
        fields = ('id', 'url', 'edema',)

        depth = 1


class EdemaDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for Edema

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            edema = Edema.objects.get(pk=pk)
            serializer = EdemaDropdownSerializer(edema, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        edema = Edema.objects.all()
        
        serializer = EdemaDropdownSerializer(
            edema, many=True, context={'request': request})
        return Response(serializer.data)

