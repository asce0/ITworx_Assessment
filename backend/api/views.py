from html import entities
from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render
from .text_analysis import azure_analysis
from .models import Entity

# Create your views here.
class EntityGatharingApiView(APIView):
    """ API EndPoint to analysis txt file with azure cognitive services"""
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """
        Description:
            - take a file from the user through request
            - read the file 
            - pass the text to azure analysis function
            - azure analysis return proccessed data
            - write the returned data into our database
        Parameters:
            - file: type(file)
        """

        # read the file from user request
        text = str(request.FILES['file'].read())
        print(text)
        print(type(text))

        # pass the read data to be analized, and store the output in dict.
        entities = azure_analysis(text)

        # iterate over the dict and write the data into database
        for key in entities:
            if key == 'b':
                continue
            else:
                Entity.objects.create(
                    name = key,
                    category = entities[key],
                )

        return Response({
            "Message": "your file is being processed!"
        })