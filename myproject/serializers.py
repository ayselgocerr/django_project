from rest_framework import serializers
from .models import Departman, Personel

class DepartmanSerializer(serializers.ModelSerializer):
    total_people = serializers.SerializerMethodField()
    class Meta:
        model = Departman
        fields = "__all__"
        read_only_fields = ["id"]
    def get_total_people(self, obj):
        return obj.total_people()   

class PersonelSerializer(serializers.ModelSerializer):
    working_days = serializers.SerializerMethodField()
    class Meta:
        model = Personel
        fields = "__all__"
        read_only_fields = ["id"]
    def get_working_days(self, obj):
        return obj.calculate_working_days()  
        