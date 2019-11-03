from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import PupilResponse
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class PupilResponseDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for PupilResponse dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = PupilResponse
        url = serializers.HyperlinkedIdentityField(
            view_name='pupilresponse',
            lookup_field='id'
        )
        fields = ('id', 'url', 'pupil_response',)

        depth = 1


class PupilResponseDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for PupilResponse

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            pupil_response = PupilResponse.objects.get(pk=pk)
            serializer = PupilResponseDropdownSerializer(pupil_response, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        pupil_response = PupilResponse.objects.all()
        
        serializer = PupilResponseDropdownSerializer(
            pupil_response, many=True, context={'request': request})
        return Response(serializer.data)

