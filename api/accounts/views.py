from rest_framework import status, permissions

from api.accounts import models

from api.accounts import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


# Create your views here.


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def all_employees(request):
    employees = models.UserProfile.objects.all()
    serializer = serializers.UserProfileSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = serializers.UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
