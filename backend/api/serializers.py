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
            "submission_date",
            "total_amount_invested",
            "final_amount",
            "change_percentage",
            "author",
            ]
        
        extra_kwargs = {"author": {"read_only": True}}