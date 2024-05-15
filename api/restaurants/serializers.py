from rest_framework import serializers
from api.restaurants import models


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ['id', 'name', 'address']


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Menu
        fields = '__all__'


class MenuChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeChoice
        fields = '__all__'


class TodayMenuSerializer(serializers.ModelSerializer):
    choices_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Menu
        fields = ['id', 'dishes', 'restaurant', 'date', 'choices_count']

    def get_choices_count(self, menu):
        return menu.employeechoice_set.count()