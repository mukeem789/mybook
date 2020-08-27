from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from usercollection.models import UserCollection
from usercollection.api.serializers import UserCollectionSerializer

# Create your views here.
# User Collection     
# ------------------------------------------------
class UserCollectionView(APIView):
    
    model = UserCollection
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user_collection_list = UserCollection.objects.all()
        serialzer = UserCollectionSerializer(user_collection_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = UserCollectionSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)