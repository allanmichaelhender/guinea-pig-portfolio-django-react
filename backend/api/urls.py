from django.urls import path
from . import views

urlpatterns = [
    path('portfolios/', views.PortfoliosListCreate.as_view(), name='portfolios-list'),
    path('portfolios/<int:pk>/', views.PortfoliosDelete.as_view(), name='portfolio-delete'),
]


