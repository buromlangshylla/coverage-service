import requests
from decouple import config
from rest_framework import serializers
from .models import Coverage, CustomerCoverage

CUSTOMER_SERVICE_URL = config("CUSTOMER_SERVICE_URL", default="http://localhost:8002")


class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'created_by', 'modified_by')


class CustomerCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCoverage
        fields = '__all__'
        read_only_fields = ('id', 'added_at', 'created_at', 'updated_at', 'created_by', 'modified_by')

    def validate_customer_id(self, value):
        url = f"{CUSTOMER_SERVICE_URL}/customers/{value}/"

        try:
            resp = requests.get(url, timeout=3)
            if resp.status_code != 200:
                raise serializers.ValidationError("Invalid customer_id: customer does not exist")
        except requests.exceptions.RequestException:
            raise serializers.ValidationError("Customer Service unavailable")

        return value

