from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FaultSerializer
from .models import Fault


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
              'Endpoint': '/fault' ,
              'method': 'GET' ,
              'body': None,
              'description': 'Returns an array of faults'
        },
        {
              'Endpoint': '/fault/id',
              'method': 'GET' ,
              'body': None,
              'description': 'Returns a single a fault object'

        },
        {
              'Endpoint': '/fault/create/',
              'method': 'POST' ,
              'body': {'body': ""},
              'description': 'Creates data for the fault'
        },
        {
              'Endpoint': '/fault/id/update/',
              'method' : 'PUT' ,
              'body' : {'body': ""},
              'description' : 'Creates an existing fault with data sent in'
        }, 
        {
              'Endpoint': '/fault/id/delete/',
              'method': 'DELETE',
              'body': None,
              'description': 'Deletes a fault'


        },   
             ]
    return Response(routes)

@api_view(['GET'])
def getFaults(reguest):
          faults = Fault.objects.all()
          serializer = FaultSerializer(faults, many=True)
          return Response(serializer.data)


@api_view(['GET'])
def getFault(reguest, pk):
          fault = Fault.objects.get(id=pk)
          serializer = FaultSerializer(fault, many=False)
          return Response(serializer.data)


@api_view(['POST'])
def createFault(request):
      data = request.data

      fault = Fault.objects.create(
            body=data['body']
      )
      serializer = FaultSerializer(fault, many=False)
      return Response(serializer.data)

@api_view(['PUT'])
def updateFault(request, pk):
    data = request.data

    fault = Fault.objects.get(id=pk)
    serializer = FaultSerializer(fault,data=request.data)
    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteFault(request, pk):
      fault = Fault.objects.get(id=pk)
      fault.delete()
      return Response('The Faults was worked on by Eng Samuel')
