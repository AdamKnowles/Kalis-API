from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import Notes, Patient
from rest_framework.decorators import action
from datetime import datetime



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for patient notes

    Arguments:
        serializers
    """

    class Meta:
        model = Notes
        url = serializers.HyperlinkedIdentityField(
            view_name='note',
            lookup_field='id'
        )
        fields = ('id', 'time', 'note', 'patient_id', 'patient')

        depth = 2


class Note(ViewSet):
    

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized vital sign instance
        """
        new_note = Notes()
        new_note.time = datetime.now()
        new_note.note = request.data["note"]
        patient = Patient.objects.get(pk=request.data["patient_id"])
        new_note.patient = patient
        new_note.save()

        serializer = NoteSerializer(new_note, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single note

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            note = Notes.objects.get(pk=pk)
            serializer = NoteSerializer(note, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        note = Notes.objects.all()
        
        serializer = NoteSerializer(
            note, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def patientnotes(self, request):
        current_patient = Patient.objects.get(pk=request.data["patient_id"])
        note = Notes.objects.all()
        note = note.filter(patient=current_patient)

        serializer = NoteSerializer(note, many=True, context={'request': request})
        return Response(serializer.data)