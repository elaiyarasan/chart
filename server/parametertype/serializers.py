from rest_framework import serializers
from .models import Parametertype

class ParametertypeSerializer(serializers.ModelSerializer):
     class Meta:
        model = Parametertype
        fields = ('parametertype','isactive','created_on','updated_on')
