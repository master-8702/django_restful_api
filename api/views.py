from django.shortcuts import render

from django.http import JsonResponse
from .models import Registrant
from .serializers import RegistrantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# in this python file we will just have a bunch of methods that will accept http request and return to the request accordingly


@api_view(['GET'])      # to limit the function on what type of requests can it handle
def registrant_list(request):
    ## here we will get all the registrants and serialize them and return them as a json file
    registrant = Registrant.objects.all()
    serializer = RegistrantSerializer(registrant, many = True)
    # here we will return json response (key:value pairs) 
    # but if want to send list of registrants just as a list rather than as an object [serialzer.data]
    # we can do it like this:  'return JsonResponse(serializer.data, safe=False)' , we set the safe to false
    # because when we are returning json it expects us to give it a key:value pair of data, and we are not giving it that
    # so we are just telling the JesonResponse just send it as a json i know what i am doing, it's intentional 

    return JsonResponse({'registrants':serializer.data}) 


