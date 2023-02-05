
from rest_framework import serializers
from .models import Registrant


class RegistrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrant
        fields = ['id', 'name', 'father_name', 'grand_father_name', 'DOB', 'POB', 'address', 'id_card', 'attachement', 'other_notes']