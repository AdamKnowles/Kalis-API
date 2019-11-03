from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import MentalStatus
from django.db import models



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class MentalStatusDropdownSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for mental status dropdown

    Arguments:
        serializers
    """
    
    class Meta:
        model = MentalStatus
        url = serializers.HyperlinkedIdentityField(
            view_name='mentalstatus',
            lookup_field='id'
        )
        fields = ('id', 'url', 'mental_status',)

        depth = 1


class MentalStatusDropdown(ViewSet):
    """Patients for Kalis"""

    

    def retrieve(self, request, pk=None):
        """Handle GET requests for single patient

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            mental_status = MentalStatus.objects.get(pk=pk)
            serializer = MentalStatusDropdownSerializer(mental_status, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        
        mental_status = MentalStatus.objects.all()
        
        serializer = MentalStatusDropdownSerializer(
            mental_status, many=True, context={'request': request})
        return Response(serializer.data)

