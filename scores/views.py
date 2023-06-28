# from django.shortcuts import render

# from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scores.models import Features
from scores.serializers import FeaturesSerializer
from django.http import Http404


@api_view(['GET','POST'])
def list_images(request, format=None):
    if request.method == 'GET':
        print('HERE')
        images = Features.objects.all()
        serializer = FeaturesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = FeaturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def image_features(request, file_name,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(pk):
        try:
            return Features.objects.get(file_name=str(pk))
        except Features.DoesNotExist:
            raise Http404

    if request.method=='GET':
        features = get_object(file_name)
        serializer = FeaturesSerializer(features)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == 'PUT':
        features = get_object(pk)
        serializer = FeaturesSerializer(features, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet = get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def image_score(request, format=None):
    """
    Calculates safety Score a given image
    """
    def get_object(self, pk):
        try:
            return Features.objects.get(pk=pk)
        except Features.DoesNotExist:
            raise Http404

    if request.method == 'GET':
        features = self.get_object(pk)
        serializer = ScoreSeriaizer(features)
        return Response(serializer.data)