from .models import Registrant
from .serializers import RegistrantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt # import


# in this python file we will just have a bunch of methods that will accept http request and return to the request accordingly


@api_view(['GET'])      # to limit the function on what type of requests can it handle
def registrant_list(request):
    ## here we will get all the registrants and serialize them and return them as a json file
    registrant = Registrant.objects.all()
    serializer = RegistrantSerializer(registrant, many = True)
    # here we will return  DRF's Reponse or json response (key:value pairs)  
    # but if we want to send list of registrants just as a list rather than as an object [serialzer.data]
    # we can do it like this:  'return JsonResponse(serializer.data, safe=False)' , we set the safe to false
    # because when we are returning json it expects us to give it a key:value pair of data, and we are not giving it that
    # so we are just telling the JesonResponse just send it as a json i know what i am doing, it's intentional 

    return Response(data={'registrants':serializer.data}, status=status.HTTP_200_OK) 



@api_view(['GET'])      # to limit the function on what type of requests can it handle
def registrant_detail(request, pk):
    ## here we will geta single registrants and serialize it and return it as a json file
    try:
        registrant = Registrant.objects.get(id=pk)

    except Registrant.DoesNotExist:
        return Response('Unknown Id',status=status.HTTP_404_NOT_FOUND)

    serializer = RegistrantSerializer(registrant, many = False) 
    return Response(data = {'registrant':serializer.data},  status=status.HTTP_200_OK) 




api_view(['POST'])
def register_registrant(request):
    # here we will register the enw registrant and return HTTP status code 201 to tell the create operation is successfull
    # but before doing that we need to check the incoming data is valid by using is_valid method from rest_framework on the data(serializer)
    # then we will save (create) the data by calling the save method on the data (serializer)
   
   
    serializer = RegistrantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



