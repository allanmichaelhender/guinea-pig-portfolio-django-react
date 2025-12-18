from django.db import models
from django.contrib.auth.models import User


class Portfolios(models.Model):
    frequency_choices = [
        ("daily", "Daily"),
        ("monthly", "Monthly"),
    ]

    investment_frequency = models.CharField(
        max_length=10, choices=frequency_choices, default="daily", blank=False
    )
    investment_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    FTSE_weight = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    SNP500_weight = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    NIKKEI225_weight = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    EUROSTOXX_weight = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    HSI_weight = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    submission_date = models.DateTimeField(auto_now_add=True)
    total_amount_invested = models.DecimalField(
        max_digits=30, decimal_places=2, default=0
    )
    final_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    change_percentage = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class FtseData(models.Model):
    date = models.DateField(primary_key=True)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    low = models.DecimalField(max_digits=20, decimal_places=2)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.BigIntegerField()
    change = models.DecimalField(max_digits=20, decimal_places=2)
    changePercent = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True
    )


class Snp500Data(models.Model):
    date = models.DateField(primary_key=True)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    low = models.DecimalField(max_digits=20, decimal_places=2)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.BigIntegerField()
    change = models.DecimalField(max_digits=20, decimal_places=2)
    changePercent = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True
    )


class Nikkei225Data(models.Model):
    date = models.DateField(primary_key=True)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    low = models.DecimalField(max_digits=20, decimal_places=2)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.BigIntegerField()
    change = models.DecimalField(max_digits=20, decimal_places=2)
    changePercent = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True
    )


class EuroStoxxData(models.Model):
    date = models.DateField(primary_key=True)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    low = models.DecimalField(max_digits=20, decimal_places=2)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.BigIntegerField()
    change = models.DecimalField(max_digits=20, decimal_places=2)
    changePercent = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True
    )

class HsiData(models.Model):
    date = models.DateField(primary_key=True)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    low = models.DecimalField(max_digits=20, decimal_places=2)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.BigIntegerField()
    change = models.DecimalField(max_digits=20, decimal_places=2)
    changePercent = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True
    )
