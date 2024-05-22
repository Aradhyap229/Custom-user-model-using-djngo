from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializer import LoginSerializer 
from.serializer import *
#from .email import *

class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            email =serializers.data['email']
            password = serializers.data['password']
            return Response({
                'status' : 200,
                'message' : 'registration successfully check email ',
                'data': serializer.data,
                 })



class RegiserAPI(APIView):

    def post( self ,request):
        try:
            data =  request.data
            serializer  = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'message' : 'registration successfully check email ',
                    'data':serializer.data,
                })
            
            return Response({
                 'status' : 400,
                 'message' : 'somethings went wrong ',
                 'data':serializer.errors,

            })
        


# Create your views here.
