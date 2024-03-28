from django.shortcuts import render,redirect
from .models import Destination
from rest_framework.authtoken.models import Token
from rest_framework import generics,permissions
from django.views import View
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import Desination_Serializer
from .exceptions import *
from django.http import Http404

class Destinations_ListAPI(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = Desination_Serializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"Success":"Your destination created suceefully"}, status=status.HTTP_201_CREATED)
        except Not_Valid_Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
class Destinations_CrudAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = Desination_Serializer
    permission_classes = [permissions.IsAuthenticated]
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"Success":"Data Updated Successfully"})
        except Http404:
            return Response({'error': 'No record found on your query,please check.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as exe:
            return Response({"error":str(exe)})
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"success":"Deleted Succesfully"},status=status.HTTP_204_NO_CONTENT)
        except Destination.DoesNotExist:
            return Response({'error':"does not exists"})
        except Http404:
            return Response({'error': 'No one record  matches the given query or given id.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class Get_Token(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = authenticate(username=username,password=password) 
             
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            if user==None or User.DoesNotExist:
                return Response({'Error': 'provide valid credentials or not existing user'})
        except Exception as exe:
            return Response({'error': str(exe)}, status=400)

class SignUp_View(APIView):
    def post(self,request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        
        try:
            if not (username and email and password):
                return Response({'error': 'Missing required fields,please provide.'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists please check once with your old credentials'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(username=username, email=email, password=password)
            if user:
                return Response({"Success": "You can get token with your ctredentials"},status=status.HTTP_201_CREATED)
        except Exception as exe:
            return Response({"Exception":str(exe)})