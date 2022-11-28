from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from tola.models import CustomUser
from .serializers import *

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class CustomUserAPIView(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            data = self.get_object(pk)
            
            serializer = CustomUserSerializer(data)

        else:

            data = CustomUser.objects.all()

            serializer = CustomUserSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        data = request.data

        serializer = CustomUserSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'User created successfully',
            'data': serializer.data,
        }

        return response

    def put(self, request, pk=None, format=None):
        CustomUser_to_update = CustomUser.objects.get(pk=pk)
        data = request.data
        serializer = CustomUserSerializer(instance=CustomUser_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response = {
            'message': 'User updated successfully',
            'data': serializer.data,
        }

        return response

