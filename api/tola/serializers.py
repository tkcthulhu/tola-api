from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class GymSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gym
        fields = ['id', 'name', 'street', 'city', 'state', 'zipcode', 'created_at']

# class CustomUserLoginSerializer(serializers.ModelField):

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username', 'password', 'first_name', 'last_name')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

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

        my_gym = user_gym.objects.get(user = id)

        my_gym = my_gym.gym

        gym = Gym.objects.get(id=my_gym.id)

        return {
            'id': gym.id,
            'name': gym.name,
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