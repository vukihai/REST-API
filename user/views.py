from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import GetAllUserSerializer
class GetAllUser(APIView):
    def get(self, request):
        user = User.objects.all()
        myData = GetAllUserSerializer(user, many=True)
        return Response(data= myData.data ,status=status.HTTP_200_OK)

