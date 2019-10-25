from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import Patient
from rest_framework.decorators import action


"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for patients

    Arguments:
        serializers
    """

    class Meta:
        model = Patient
        url = serializers.HyperlinkedIdentityField(
            view_name='patient',
            lookup_field='id'
        )
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'sex', 'diagnosis')

        


class Patients(ViewSet):
    """Patients for Kalis"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized patient instance
        """
        new_patient = Patient()
        new_patient.first_name = request.data["first_name"]
        new_patient.last_name = request.data["last_name"]
        new_patient.birth_date = request.data["birth_date"]
        new_patient.sex = request.data["sex"]
        new_patient.diagnosis = request.data["diagnosis"].lower()
        new_patient.save()

        serializer = PatientSerializer(new_patient, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single patient

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a patient

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            patient = Patient.objects.get(pk=pk)
            patient.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Patient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        patients = Patient.objects.all()
        patient_list = []

        limit = self.request.query_params.get('limit', None)
        if limit is not None:
            patients = Patient.objects.all()[:int(limit)]

        
        serializer = PatientSerializer(
            patients, many=True, context={'request': request})
        return Response(serializer.data)

    