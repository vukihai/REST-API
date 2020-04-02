from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Intent, Rasalog
from .serializers import UserSerializer, IntentSerializer, RasalogSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.core import serializers
import pandas as pd
@csrf_exempt
@api_view(['GET','POST'])
def user(request):
    """
    List all user, or create a new user.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        #return JsonResponse(serializer.errors, status=400)
@csrf_exempt
@api_view(['GET','PUT'])
def user_detail(request, pk):
    """
    Get, Update user.
    """
    try:
        user = User.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(data= serializer.data, safe=False)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data= serializer.data, safe=False)


@csrf_exempt
@api_view(['GET','POST'])
def intent(request):
    """
    get all intent_count
    """
    if request.method == 'GET':
        if request.method == 'GET':
            intent = Intent.objects.all()
        serializer = IntentSerializer(intent, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IntentSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
@csrf_exempt
@api_view(['GET', 'POST'])
def intent_detail(request, pk):
    """
    Get, Update a intent
    """
    try:
        intent = Intent.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        #result = []
        result = list(Intent.objects.order_by('quantity')[:5])
        #serializer = IntentSerializer(result)
        serializer = serializers.serialize('json', result)
        return HttpResponse(serializer, content_type='application/json')
    if request.method == 'POST':
        data = intent
        data.quantity = data.quantity + 1
        serializer = IntentSerializer(intent, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe= False)
    return Response({'key': 'value'}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET', 'POST'])
def rasalog(request):
    """
     save log to db
    """
    if request.method == 'GET':
        rasalog = Rasalog.objects.all()
        serializer = RasalogSerializer(rasalog, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RasalogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return Response({}, status=status.HTTP_200_OK)