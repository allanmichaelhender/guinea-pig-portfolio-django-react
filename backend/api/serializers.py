from email.policy import default
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Portfolios


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class PortfoliosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolios
        fields = [
            "id",
            "investment_frequency",
            "investment_amount",
            "start_date",
            "end_date",
            "FTSE_weight",
            "SNP500_weight",
            "NIKKEI225_weight",
            "EUROSTOXX_weight",
            "HSI_weight",
            "submission_date",
            "total_amount_invested",
            "final_amount",
            "change_percentage",
            "author",
        ]

        extra_kwargs = {
            "author": {"read_only": True},
            "submission_date": {"read_only": True},
            "total_amount_invested": {"read_only": True},
            "final_amount": {"read_only": True},
            "change_percentage": {"read_only": True},
        }

class PortfoliosGuestSerializer(serializers.Serializer):
    investment_frequency = serializers.CharField()
    investment_amount = serializers.DecimalField(decimal_places=2, default=0)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    FTSE_weight = serializers.DecimalField(decimal_places=2, default=0)
    SNP500_weight = serializers.DecimalField(decimal_places=2, default=0)
    NIKKEI225_weight = serializers.DecimalField(decimal_places=2, default=0)
    EUROSTOXX_weight = serializers.DecimalField(decimal_places=2, default=0)
    HSI_weight = serializers.DecimalField(decimal_places=2, default=0)
    total_amount_invested = serializers.DecimalField(decimal_places=2, default=0)
    final_amount = serializers.DecimalField(decimal_places=2, default=0)
    change_percentage = serializers.DecimalField(max_digits=8, decimal_places=4, default=0)


    