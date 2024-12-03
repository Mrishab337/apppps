from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import BusinessDetails
from .serializers import BusinessSerializer


# Create your views here.

class BusinessCreateView(viewsets.ModelViewSet):
    queryset = BusinessDetails.objects.all()
    serializer_class = BusinessSerializer