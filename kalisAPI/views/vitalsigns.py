from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import VitalSigns, Patient



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class VitalSignSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for vital signs

    Arguments:
        serializers
    """

    class Meta:
        model = VitalSigns
        url = serializers.HyperlinkedIdentityField(
            view_name='vitalsign',
            lookup_field='id'
        )
        fields = ('id', 'time', 'temperature', 'heart_rate', 'blood_pressure', 'respiration_rate', 'oxygen_saturation', 'patient')

        depth = 1


class VitalSign(ViewSet):
    """Patients for Kalis"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized vital sign instance
        """
        new_vitalsign = VitalSigns()
        new_vitalsign.time = request.data["time"]
        new_vitalsign.temperature = request.data["temperature"]
        new_vitalsign.heart_rate = request.data["heart_rate"]
        new_vitalsign.blood_pressure = request.data["blood_pressure"]
        new_vitalsign.respiration_rate = request.data["respiration_rate"]
        new_vitalsign.oxygen_saturation = request.data["oxygen_saturation"]
        patient = Patient.objects.get(pk=request.data["patient_id"])
        new_vitalsign.patient = patient
        new_vitalsign.save()

        serializer = VitalSignSerializer(new_vitalsign, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single vital sign set

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            vitalsign = VitalSigns.objects.get(pk=pk)
            serializer = VitalSignSerializer(vitalsign, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a patient

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            vitalsign = VitalSigns.objects.get(pk=pk)
            vitalsign.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except VitalSigns.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        vitalsigns = VitalSigns.objects.all()
        
        serializer = VitalSignSerializer(
            vitalsigns, many=True, context={'request': request})
        return Response(serializer.data)
