from rest_framework import serializers
from customer_and_user_management.serializer import (
    UserSerializer, CustomerSerializer
)
from contract.serializer import ContractSerializer
from contract_review_approval.models import (
    ContractActivityLog, ContractApprover, Metadata,
    ContractMetadata, ContractReviewer
)


class ContractReviewerSerializer(serializers.ModelSerializer):
    """Serializer for the ContractReviewer model."""
    # user_id = UserSerializer()
    # contract_id = ContractSerializer()

    class Meta:
        model = ContractReviewer
        fields = '__all__'


class ContractActivityLogSerializer(serializers.ModelSerializer):
    """Serializer for the ContractActivityLog model."""
    # user_id = UserSerializer()
    # contract_id = ContractSerializer()
    # customer_id = CustomerSerializer()

    class Meta:
        model = ContractActivityLog
        fields = '__all__'


class ContractApproverSerializer(serializers.ModelSerializer):
    """Serializer for the ContractApprover model."""
    # user_id = UserSerializer()
    # contract_id = ContractSerializer()

    class Meta:
        model = ContractApprover
        fields = '__all__'


class MetadataSerializer(serializers.ModelSerializer):
    """Serializer for the Metadata model."""

    class Meta:
        model = Metadata
        fields = '__all__'


class ContractMetadataSerializer(serializers.ModelSerializer):
    """Serializer for the ContractMetadata model."""
    # metadata_id = MetadataSerializer()
    # contract_id = ContractSerializer()
    # added_by_user_id = UserSerializer()

    class Meta:
        model = ContractMetadata
        fields = '__all__'
