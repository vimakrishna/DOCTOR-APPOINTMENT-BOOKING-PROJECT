from django.shortcuts import render,get_object_or_404
from clinic.models import DoctorDb,AppointmentDb
from clinic.serializers import Doctor_Serializer,Appointment_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import time,timedelta,datetime
from rest_framework import serializers





# Create your views here
class DoctorListCreateView(APIView):
    def get(self, request):
        qs = DoctorDb.objects.all()
        serializer_instance = Doctor_Serializer(qs, many=True)
        return Response(data=serializer_instance.data) 

    def post(self, request):
        form_data = request.data
        serializer_instance = Doctor_Serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class DoctorRetreiveDeleteView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(DoctorDb, id=pk)
        serializer_instance = Doctor_Serializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        doctor_object = get_object_or_404(DoctorDb,id = pk)
        serializer_instance = Doctor_Serializer(data=form_data, instance = doctor_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        doctor_object = get_object_or_404(DoctorDb, id=pk)
        doctor_object.delete()
        return Response(data={
            "Message":"Deleted..!"
        })

class AppoinmentListCreateView(APIView):
    def get(self, request):
            qs = AppointmentDb.objects.all()
            serializer_instance = Appointment_serializer(qs, many=True)
            return Response(data=serializer_instance.data) 

    
    def post(self, request):
        form_data = request.data
        serializer_instance = Appointment_serializer(data=form_data)
        if serializer_instance.is_valid():
            print(serializer_instance.validated_data)
            Appointment_date = serializer_instance.validated_data.get("Appointment_date")
            Doctor_id = serializer_instance.validated_data.get("Doctor_id")
            last_appointment = AppointmentDb.objects.filter(Appointment_date=Appointment_date,Doctor_id=Doctor_id).order_by("-Token_number").first()
            if last_appointment is None:
                form_data["Token_number"] = 1
                form_data["Appointment_time"] = time(10, 0)
            else:
                form_data["Token_number"] = last_appointment.Token_number + 1
                current_time = datetime.combine(Appointment_date,last_appointment.Appointment_time)
                next_time = current_time + timedelta(minutes=15)
                

                #Adding Lunch Break time
                if next_time.time() == time(10, 15):
                    next_time = datetime.combine(Appointment_date,time(13, 30))

                elif next_time.time() == time(14,15):
                    return Response(data={
                        "Message":"Dr not available"
                    })
                
                form_data["Appointment_time"] = next_time.time()
                
            qs = AppointmentDb.objects.create(**form_data)
            serializer_instance = Appointment_serializer(qs)
            
            return Response(data={
            "Message": "Booked Successfully..!",
            "Token Number is": form_data["Token_number"],
            "Appointment Time is": form_data["Appointment_time"]
        })
        else:
            return Response(serializer_instance.errors)

        




    

