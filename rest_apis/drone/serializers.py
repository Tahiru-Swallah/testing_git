from rest_framework import serializers
from .models import DroneCategory, Drone, Pilot, Competition
from django.contrib.auth.models import User

class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = [
            'url',
            'name'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(
        many=True, 
        read_only = True
    )

    class Meta:
        model = User
        fields = [
            'url',
            'pk',
            'username',
            'drones'
        ]



class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'drone-detail'
    )

    class Meta:
        model = DroneCategory
        fields = [
            'url',
            'id',
            'name',
            'drones'
        ]

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset=DroneCategory.objects.all(), slug_field = 'name'
    )

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=Drone
        fields = [
            'url',
            'id',
            'name',
            'manufacturing_date',
            'owner',
            'has_it_competed',
            'inserted_timespan',
            'drone_category'
        ]

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
 # Display all the details for the related drone
    drone = DroneSerializer()
    class Meta:
        model = Competition
        fields = [
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone'
        ]

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Pilot.GENDER_CHOICE
    )
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )
    class Meta:
        model = Pilot
        fields = [
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timespan',
            'competitions'
        ]


class PilotCompetitionSerializer(serializers.ModelSerializer):
    # Display the pilot's name
    pilot = serializers.SlugRelatedField(
        queryset=Pilot.objects.all(),
        slug_field='name'
    )
    # Display the drone's name
    drone = serializers.SlugRelatedField(
        queryset=Drone.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Competition
        fields = [
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'pilot',
            'drone'
        ]