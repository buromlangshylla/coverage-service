from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Coverage, CustomerCoverage
from .permissions import IsJWTAuthenticated
from .serializers import CoverageSerializer, CustomerCoverageSerializer


class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_permissions(self):
        if self.action  in ['create', 'update', 'partial_update', 'destroy']:
            return [IsJWTAuthenticated()]
        return [AllowAny()]


class CustomerCoverageViewSet(viewsets.ModelViewSet):
    queryset = CustomerCoverage.objects.all()
    serializer_class = CustomerCoverageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer_id', 'policy_id', 'status']

    def get_permissions(self):
        if self.action  in ['create', 'update', 'partial_update', 'destroy']:
            return [IsJWTAuthenticated()]
        return [AllowAny()]

    @action(detail=False, methods=['get'], url_path='(?P<customer_id>[^/.]+)')
    def customer_coverages(self, request, customer_id=None):
        queryset = self.get_queryset().filter(customer_id=customer_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
