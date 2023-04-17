from rest_framework import serializers

from .models import LeadModel

# Create here
class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadModel
        fields = '__all__'