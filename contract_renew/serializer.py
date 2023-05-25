from rest_framework import serializers
from contract_renew.models import RenewContract, UploadContract, UploadedContractStatus


class UploadContractSerializer(serializers.ModelSerializer):
    """Serializer for the UploadContract model."""
    class Meta:
        model = UploadContract
        fields = '__all__'


class RenewContractSerializer(serializers.ModelSerializer):
    """Serializer for the RenewContract model."""
    class Meta:
        model = RenewContract
        fields = '__all__'


class UploadedContractStatusSerializer(serializers.ModelSerializer):
    """Serializer for the UploadedContractStatus model."""
    class Meta:
        model = UploadedContractStatus
        fields = '__all__'
