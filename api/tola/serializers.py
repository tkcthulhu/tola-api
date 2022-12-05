from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class GymSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gym
        fields = ['id', 'name', 'street', 'city', 'state', 'zipcode', 'created_at']

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    gym = serializers.SerializerMethodField()

    maxes = serializers.SerializerMethodField()

    class Meta:

        model = CustomUser

        fields = ['id', 'username', 'first_name', 'last_name', 'birthday', 'email', 'groups', 'is_coach', 'gym', 'maxes', 'password', 'weight']

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def get_gym(self, obj):

        id = obj.id

        if user_gym.objects.filter(user=id):
            pass
        else:
            return ''

        my_gym = user_gym.objects.get(user = id, active=True)

        user_gym_id = my_gym.id

        my_gym = my_gym.gym

        gym = Gym.objects.get(id=my_gym.id)

        return {
            'id': gym.id,
            'name': gym.name,
            'user_gym_id': user_gym_id
        }

    def get_maxes(self, obj):

        id = obj.id

        if not Max.objects.filter(user=id):
            return []

        my_maxes = Max.objects.filter(user = id)

        my_current_maxes = my_maxes.filter(active = True)

        maxes = []

        for max in my_current_maxes:

            exercise = Exercise.objects.get(id = max.exercise.id)

            maxes.append({
                'id': max.id,
                'exercise_id': exercise.id,
                'exercise': exercise.name,
                'weight': max.weight,
                'reps': max.num_of_reps,
                'date': max.created_at
            })

        return maxes

class MaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Max
        fields = ['id', 'user', 'exercise', 'weight', 'num_of_reps', 'active', 'created_at']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name']

class UserGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_gym
        fields = ['id', 'user', 'gym', 'active', 'date_joined']

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['id', 'name', 'street', 'city', 'state', 'zipcode']

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'coach', 'created_at', 'updated_at']

class program_sessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = program_session
        fields = ['id', 'program', 'day']

class program_session_exerciseSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = program_session_exercise
        fields = ['id', 'program_session', 'exercise', 'max_exercise']

class program_session_exercise_setSerializer(serializers.ModelSerializer):
    class Meta:
        model = program_session_exercise_set
        fields = ['id', 'athlete', 'program_session_exercise', 'set_num', 'num_of_reps', 'percent']

class user_programSerializer(serializers.ModelSerializer):

    athlete = serializers.SerializerMethodField()

    program = serializers.SerializerMethodField()

    class Meta:

        model = user_program

        fields = ['id', 'athlete', 'program']

    def get_athlete(self, obj):

        return obj.athlete.username

    def get_program(self, obj):

        program_id = obj.program.id

        coach = obj.program.coach

        sessions = program_session.objects.filter(program = program_id)

        sessions_list = []

        for session in sessions:

            exercises=program_session_exercise.objects.filter(program_session=session.id)

            exercise_list = []

            for exercise in exercises:

                exercise_id = exercise.exercise.id

                sets = program_session_exercise_set.objects.filter(program_session_exercise=exercise.id).order_by('set_num')

                set_list = []

                for x in sets:

                    print(x.percent)

                    set_list.append({
                      "set_num": x.set_num,
                      "num_of_reps": x.num_of_reps,
                      "percent": x.percent
                    })

                exercise_list.append({
                    "exercise": exercise.exercise.name,
                    "sets": set_list
                })

            sessions_list.append({
                "session": session.day,
                "exercises": exercise_list
            })

        response = {
            "program": obj.program.name,
            "coach": coach.username,
            "sessions": sessions_list
        }

        return response

