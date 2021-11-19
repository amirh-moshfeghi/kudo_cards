from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class RetrieveUpdateDestroyUserAPIView(RetrieveUpdateDestroyAPIView):
    User = get_user_model()
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
