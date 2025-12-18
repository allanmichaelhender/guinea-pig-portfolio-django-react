from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PortfoliosSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Portfolios
from .investing_funcitons import invest


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
            investment_frequency = serializer.validated_data.get("investment_frequency")
            investment_amount = serializer.validated_data.get("investment_amount")
            start_date = serializer.validated_data.get("start_date")
            end_date = serializer.validated_data.get("end_date")
            FTSE_weight = serializer.validated_data.get("FTSE_weight")
            SNP500_weight = serializer.validated_data.get("SNP500_weight")
            NIKKEI225_weight = serializer.validated_data.get("NIKKEI225_weight")

            computed_values = invest(
                investment_frequency,
                investment_amount,
                start_date,
                end_date,
                FTSE_weight,
                SNP500_weight,
                NIKKEI225_weight,
            )


            change_percentage = (float(computed_values["end_value"])-float(computed_values["total_invested"]))/float(computed_values["total_invested"])

            serializer.save(
                author=self.request.user, 
                total_amount_invested = float(computed_values["total_invested"]),
                final_amount = float(computed_values["end_value"]),
                change_percentage=change_percentage
            )
        else:
            print(serializer.errors)


class PortfoliosDelete(generics.DestroyAPIView):
    serializer_class = PortfoliosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Portfolios.objects.filter(author=user)
