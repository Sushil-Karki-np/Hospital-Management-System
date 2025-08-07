from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from hospital.models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        doctor = self.get_object()
        doctor.status = True
        doctor.save()
        return Response({'status': 'Doctor approved'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        doctor = self.get_object()
        doctor.status = False
        doctor.save()
        return Response({'status': 'Doctor rejected'})


