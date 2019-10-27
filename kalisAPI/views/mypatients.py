# from django.http import HttpResponseServerError
# from django.contrib.auth.models import User
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework import status
# from kalisAPI.models import Patient
# from kalisAPI.models import MyPatients
# from .patient import PatientSerializer

# """Author: Adam Knowles
# Purpose: Allow a user to communicate with the Kalise database to GET POST and DELETE entries for mypatients.
# Methods: GET DELETE(id) POST"""


# class MyPatientSerializer(serializers.HyperlinkedModelSerializer):
#     """JSON serializer for mypatients
#     Arguments:
#         serializers
#     """

#     class Meta:
#         model = MyPatients
#         url = serializers.HyperlinkedIdentityField(
#             view_name='mypatients',
#             lookup_field='id'
#         )
#         fields = ('id', 'url', 'patient', 'user_id')

#         depth = 1


# class MyPatient(ViewSet):
#     """Orders for BangazonApp"""

#     def retrieve(self, request, pk=None):
#         """Handle GET requests for single orderproduct
#         Returns:
#             Response -- JSON serialized orderproduct instance
#         """
#         try:
#             mypatient = MyPatients.objects.get(pk=pk)
#             serializer = MyPatientSerializer(mypatient, context={'request': request})
#             return Response(serializer.data)
#         except Exception as ex:
#             return HttpResponseServerError(ex)

    

#     def list(self, request):
#         """Handle GET requests to orderproducts resource
#         Returns:
#             Response -- JSON serialized list of orderproducts
#         """
#         mypatients = MyPatients.objects.all()

#         order = self.request.query_params.get('order', None)
#         product = self.request.query_params.get('product', None)
#         payment = self.request.query_params.get('payment', None)

#         if product is not None:
#             orderproducts = orderproducts.filter(product__id=product)
#         if order is not None:
#             orderproducts = orderproducts.filter(order_payment=None)
        


#         serializer = OrderProductSerializer(
#             orderproducts, many=True, context={'request': request})
#         return Response(serializer.data)