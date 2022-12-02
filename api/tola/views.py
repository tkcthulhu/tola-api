from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from tola.models import *
from .serializers import *

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class UserGymViewSet(viewsets.ModelViewSet):
    queryset = user_gym.objects.all().order_by('id')
    serializer_class = UserGymSerializer
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

        response.data = {
            'message': 'User updated successfully',
            'data': serializer.data,
        }

        return response

class MaxAPIView(APIView):

    def get_object(self, pk):

        try:

            return Max.objects.get(pk=pk)

        except Max.DoesNotExist:

            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            
            data = self.get_object(pk)
            
            serializer = MaxSerializer(data)

        else:

            data = Max.objects.all().order_by('id')

            serializer = MaxSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        data = request.data

        serializer = MaxSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'Max created successfully',
            'data': serializer.data,
        }

        return response

    def put(self, request, pk=None, format=None):

        Max_to_update = Max.objects.get(pk=pk)

        data = request.data

        serializer = MaxSerializer(instance=Max_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Max updated successfully',
            'data': serializer.data,
        }

        return response

class ExerciseAPIView(APIView):

    def get_object(self, pk):

        try:

            return Exercise.objects.get(pk=pk)

        except Exercise.DoesNotExist:

            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            
            data = self.get_object(pk)
            
            serializer = ExerciseSerializer(data)

        else:

            data = Exercise.objects.all().order_by('id')

            serializer = ExerciseSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        data = request.data

        serializer = ExerciseSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'Exercise created successfully',
            'data': serializer.data,
        }

        return response

    def put(self, request, pk=None, format=None):

        Exercise_to_update = Exercise.objects.get(pk=pk)

        data = request.data

        serializer = ExerciseSerializer(instance=Exercise_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Exercise updated successfully',
            'data': serializer.data,
        }

        return response

class UserGymAPIView(APIView):

    def get_object(self, pk):

        try:

            return user_gym.objects.get(pk=pk)

        except user_gym.DoesNotExist:

            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:

            data = self.get_object(pk)
            
            serializer = UserGymSerializer(data)

        else:

            data = user_gym.objects.all()

            serializer = UserGymSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        data = request.data

        serializer = UserGymSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'User created successfully',
            'data': serializer.data,
        }

        return response

    def put(self, request, pk=None, format=None):

        UserGym_to_update = user_gym.objects.get(pk=pk)

        data = request.data

        serializer = UserGymSerializer(instance=UserGym_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'User updated successfully',
            'data': serializer.data,
        }

        return response

class GymAPIView(APIView):

    def get_object(self, pk):

        try:

            return Gym.objects.get(pk=pk)

        except Gym.DoesNotExist:

            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            
            data = self.get_object(pk)
            
            serializer = GymSerializer(data)

        else:

            data = Gym.objects.all().order_by('id')

            serializer = GymSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        data = request.data

        serializer = GymSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'Gym created successfully',
            'data': serializer.data,
        }

        return response

    def put(self, request, pk=None, format=None):

        Gym_to_update = Gym.objects.get(pk=pk)

        data = request.data

        serializer = GymSerializer(instance=Gym_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Gym updated successfully',
            'data': serializer.data,
        }

        return response