from django.urls import path
from . import views

urlpatterns = [
    path('portfolios/', views.PortfoliosListCreate.as_view(), name='note-list'),
    path('portfolios/delete/<int:pk>/', views.PortfoliosDelete.as_view(), name='delete-note'),
]


