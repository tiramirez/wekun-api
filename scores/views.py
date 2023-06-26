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
    def get(self):
        images = Features.objects.all()
        serializer = FeaturesSerializer(images, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = FeaturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def image_features(request, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Features.objects.get(pk=pk)
        except Features.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        features = self.get_object(pk)
        serializer = FeaturesSerializer(features)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        features = self.get_object(pk)
        serializer = FeaturesSerializer(features, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)