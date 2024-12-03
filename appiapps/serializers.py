from rest_framework import serializers
from .models import BusinessDetails

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDetails
        fields = ['business_name', 'phone_number', 'address', 'create_work_space_name']
