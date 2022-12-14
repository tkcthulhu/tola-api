from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

class user_programViewSet(viewsets.ModelViewSet):
    queryset = user_program.objects.all().order_by('id')
    serializer_class = user_programSerializer
    permission_classes = [permissions.AllowAny]

class user_setViewSet(viewsets.ModelViewSet):
    queryset = user_set.objects.all().order_by('athlete', 'id')
    serializer_class = user_setSerializer
    permission_classes = [permissions.AllowAny]

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
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

@api_view([ 'POST', 'GET'])
def addUserToProgram(request, program_id):

    user = CustomUser.objects.get(id=request.user.id)
    program = Program.objects.get(id=program_id)

    if request.method == "POST":

        post = "Program joined successfully"

        try:

            this_user_program = user_program.objects.get(athlete=user, program=program)

            current_programs = user_program.objects.filter(athlete=user.id)

            for program in current_programs:

                program.active = False

                program.save()

            this_user_program.active = True

            this_user_program.save()

            return Response('Program has been rejoined')

        except user_program.DoesNotExist:

            try:

                current_programs = user_program.objects.filter(athlete=user.id)

                for program in current_programs:

                    program.active = False

                    program.save()

            except:

                pass

            user_program.objects.create(athlete=user, program=Program.objects.get(id=program_id))

            sessions = program_session.objects.filter(program=program_id)

            for session in sessions:

                exercises = program_session_exercise.objects.filter(program_session=session.id)

                for exercise in exercises:

                    sets = program_session_exercise_set.objects.filter(program_session_exercise=exercise.id).order_by('id')

                    for x in sets:

                        start_status = SetStatus.objects.get(id=1)

                        user_set.objects.create(athlete=user, session_set=x, status=start_status)


        return Response(post)

@api_view(['PATCH', 'DELETE'])
def updateUserProgram(request, program_id):

    user = CustomUser.objects.get(id = request.user.id)
    program = Program.objects.get(id = program_id)

    if request.method == 'PATCH':

        sessions = program_session.objects.filter(program=program_id)

        for session in sessions:

            exercises = program_session_exercise.objects.filter(program_session=session.id)

            for exercise in exercises:

                sets = program_session_exercise_set.objects.filter(program_session_exercise=exercise.id).order_by('id')

                for x in sets:

                    this_set = user_set.objects.get(session_set=x.id, athlete=user.id)

                    this_set.status = SetStatus.objects.get(id=1)

                    this_set.save()
        return Response('Program has been reset')

    if request.method == 'DELETE':

        userProgram = user_program.objects.get(athlete=user.id, program=program.id)

        userProgram.active = False

        userProgram.save()

        return Response('You have left this program')
