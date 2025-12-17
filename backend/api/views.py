from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PortfoliosSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Portfolios

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class PortfoliosListCreate(generics.ListCreateAPIView):
    serializer_class = PortfoliosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Portfolios.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class PortfoliosDelete(generics.DestroyAPIView):
    serializer_class = PortfoliosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Portfolios.objects.filter(author=user)