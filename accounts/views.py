from datetime import datetime
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from .models import User

# Create your views here.

class signupAPIview(APIView):
    def post(self,request):
        data = request.data
        email = data.get('email')
        username = data.get('username')

        if not (email or not username):
            return Response({"error": "email and username is required"},status=400)
        if get_user_model().objects.filter(email=email).exists():
            return Response({"error": "email is required"},status=400)
        if get_user_model().objects.filter(username=username).exists():
            return Response({"error": "username is required"}, status=400)

        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password= data.get('password'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),

        )
        return Response(
            {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        },status=201)
    
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)