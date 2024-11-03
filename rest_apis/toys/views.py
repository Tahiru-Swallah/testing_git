from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ToySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Toy

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET', 'POST'])
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        serializer = ToySerializer(toys, many=True)
        return JSONResponse(serializer.data)
    
    elif request.method == 'POST':
        serializer = ToySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ToySerializer(toy)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = ToySerializer(toy, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        toy.delete()
        return JSONResponse(status=status.HTTP_204_NO_CONTENT)