from rest_framework import serializers
from .models import UserInfo

# Well it takes all the columns in our db and serializes them. 
class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'