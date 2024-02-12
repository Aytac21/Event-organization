from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from .models import User, EventUser, Organizer
from .serializers import CustomUserSerializer, EventUserSerializer, OrganizerSerializer,UserProfileSerializer

class EventUserRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_parent=True)
            EventUser.objects.create(user=user)
            return Response({'message': 'Parent registered successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizerRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_teacher=True)
            Organizer.objects.create(user=user)
            return Response({'message': 'Teacher registered successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventUserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password, is_parent=True)

        if user is not None:
            login(request, user)
            serializer = EventUserSerializer(user.parent)
            return Response({'message': 'Parent login successful', 'user': serializer.data})
        return Response({'message': 'Parent login failed'}, status=status.HTTP_401_UNAUTHORIZED)

class OrganizerLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password, is_teacher=True)

        if user is not None:
            login(request, user)
            serializer = OrganizerSerializer(user.teacher)
            return Response({'message': 'Teacher login successful', 'user': serializer.data})
        return Response({'message': 'Teacher login failed'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'})

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
