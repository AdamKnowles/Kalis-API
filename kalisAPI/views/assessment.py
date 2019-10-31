from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kalisAPI.models import Patient, Assessment
from rest_framework.decorators import action
from datetime import datetime
from datetime import date



"""Author: Adam Knowles
Purpose: Allow a user to communicate with the Kalis database to GET POST and DELETE entries.
Methods: GET DELETE(id) POST"""


class AssessmentSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for assessments

    Arguments:
        serializers
    """

    class Meta:
        model = Assessment
        url = serializers.HyperlinkedIdentityField(
            view_name='assessments',
            lookup_field='id'
        )
        fields = ('id', 'time', 'mental_status', 'pupil_response', 'heart_sounds', 'breath_sounds', 'edema', 'oxygen_rate', 'bowel_sounds', 'npo', 'last_bowel_movement', 'urine_color', 'urine_odor', 'urine_amount', 'patient_id', 'patient')

        depth = 1


class Assessments(ViewSet):
    """Assessments for Kalis"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized vital sign instance
        """
        new_assessment = Assessment()
        new_assessment.time = datetime.now()
        new_assessment.mental_status = request.data["mental_status"]
        new_assessment.pupil_response = request.data["pupil_response"]
        new_assessment.heart_sounds = request.data["heart_sounds"]
        new_assessment.breath_sounds = request.data["breath_sounds"]
        new_assessment.edema = request.data["edema"]
        new_assessment.oxygen_rate = request.data["oxygen_rate"]
        new_assessment.bowel_sounds = request.data["bowel_sounds"]
        new_assessment.npo = request.data["npo"]
        new_assessment.last_bowel_movement = request.data["last_bowel_movement"]
        new_assessment.urine_color = request.data["urine_color"]
        new_assessment.urine_odor = request.data["urine_odor"]
        new_assessment.urine_amount = request.data["urine_amount"]
        patient = Patient.objects.get(pk=request.data["patient_id"])
        new_assessment.patient = patient
        new_assessment.save()

        serializer = AssessmentSerializer(new_assessment, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single vital sign set

        Returns:
            Response -- JSON serialized patient instance
        """
        try:
            
            assessment = Assessment.objects.get(pk=pk)
            serializer = AssessmentSerializer(assessment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def update(self, request, pk=None):
        """Handle PUT requests for an individual vitalsign
        Returns:
            Response -- Empty body with 204 status code
        """
        updated_assessment = Assessment.objects.get(pk=pk)
        updated_assessment.mental_status = request.data["mental_status"]
        updated_assessment.pupil_response = request.data["pupil_response"]
        updated_assessment.heart_sounds = request.data["heart_sounds"]
        updated_assessment.breath_sounds = request.data["breath_sounds"]
        updated_assessment.edema = request.data["edema"]
        updated_assessment.oxygen_rate = request.data["oxygen_rate"]
        updated_assessment.bowel_sounds = request.data["bowel_sounds"]
        updated_assessment.npo = request.data["npo"]
        updated_assessment.last_bowel_movement = request.data["last_bowel_movement"]
        updated_assessment.urine_color = request.data["urine_color"]
        updated_assessment.urine_odor = request.data["urine_odor"]
        updated_assessment.urine_amount = request.data["urine_amount"]
        updated_assessment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a patient

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            assessment = Assessment.objects.get(pk=pk)
            assessment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Assessment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to patients resource

        Returns:
            Response -- JSON serialized list of patients 
        """

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        assessments = Assessment.objects.all().order_by('id').reverse()
        
        serializer = AssessmentSerializer(
            assessments, many=True, context={'request': request})
        return Response(serializer.data)



    @action(methods=['get'], detail=False)
    def patientassessments(self, request):
        current_patient = Patient.objects.get().pk
        assessments = Assessment.objects.all()
        assessments = assessments.filter(patient=current_patient)

        serializer = AssessmentSerializer(assessments, many=True, context={'request': request})
        return Response(serializer.data)
