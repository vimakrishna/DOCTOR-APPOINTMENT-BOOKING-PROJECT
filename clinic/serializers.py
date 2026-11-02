from rest_framework import serializers
from clinic.models import DoctorDb,AppointmentDb
from django.utils import timezone

class Doctor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDb
        fields = "__all__"

        #fields = ["all","Doctor_name","Specialization"]

        read_only_fields = ["id"]

# Automatic field generation
# Default validations
# Conversion between model instances and serialized data
# class Meta:Defines the Serializer's configuration

class Appointment_serializer(serializers.ModelSerializer):
    class Meta:
            model = AppointmentDb
            fields = "__all__"
            read_only_fields = ["id"]

    def validate(self, validated_data):
        Phone = validated_data.get("Phone")
        Appointment_date = validated_data.get("Appointment_date")

        if Appointment_date < timezone.localdate():
             raise serializers.ValidationError("Select a valid date...!  ")

        if AppointmentDb.objects.filter(
             Phone=Phone,
             Appointment_date=Appointment_date).exists():
             raise serializers.ValidationError("Already Booked...!")
        else:
             return validated_data

        
                     

        
        

    
