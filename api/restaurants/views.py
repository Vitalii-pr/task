from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt import authentication
from api.restaurants.permissions import IsOwnerOrReadOnly
from datetime import datetime

from api.restaurants.models import Restaurant, Menu, EmployeeChoice
from api.restaurants.serializers import RestaurantSerializer, MenuSerializer, MenuChoiceSerializer, TodayMenuSerializer

from api.accounts import models


# Create your views here.

class RestaurantModelViewSet(viewsets.ModelViewSet):
    """restaurant model viewset"""
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    authentication_classes = [authentication.JWTAuthentication,]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def add_restaurant_admin(self, request, pk=None):

        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"message": f"No user found"}, status=status.HTTP_400_BAD_REQUEST)

        restaurant = self.get_object()
        user = get_object_or_404(models.UserProfile, pk=user_id)
        if restaurant and user:
            restaurant.admin = user
            restaurant.save()
            return Response({"message": f"{user.name} added as admin to {restaurant.name}"}, status=status.HTTP_200_OK)
        return Response({"message": f"No restaurant or user found"}, status=status.HTTP_400_BAD_REQUEST)


class MenuModelViewSet(viewsets.ReadOnlyModelViewSet):
    """menu model view set"""
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upload_menu_to_restaurant(request):

    user = request.user

    restaurant = Restaurant.objects.filter(admin=user).first()

    if not restaurant:
        return Response({'message': "You don't have restaurants to add menus"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MenuSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(restaurant=restaurant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def vote_for_menu(request, pk=None):
    menu = get_object_or_404(Menu, pk=pk)
    user = request.user
    choice = MenuChoiceSerializer(data={"user": user.id, "menu": menu.id})
    if choice.is_valid() and not EmployeeChoice.objects.filter(user=user, menu=menu).first():
        choice.save()
        return Response({"message": "Successfully voted"}, status=status.HTTP_200_OK)
    return Response(choice.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_ranking(request):
    today = datetime.today()
    menus = Menu.objects.filter(date__gte=today)
    serializer = TodayMenuSerializer(menus, many=True)
    return Response(serializer.data)

