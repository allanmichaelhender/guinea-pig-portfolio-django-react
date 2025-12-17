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
            "author",
            ]
        
        extra_kwargs = {"author": {"read_only": True}}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['investment_amount'].initial = 0
        self.fields['FTSE_weight'].initial = 0
        self.fields['SNP500_weight'].initial = 0
        self.fields['NIKKEI225_weight'].initial = 0
