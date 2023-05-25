from lables.models import ContractFolder, ContractLable, LabelMaster
from rest_framework import serializers


class LabelMasterSerializer(serializers.ModelSerializer):
    """Serializer class for LabelMaster model."""
    class Meta:
        model = LabelMaster
        fields = '__all__'


class ContractLableSerializer(serializers.ModelSerializer):
    """Serializer class for ContractLable model."""
    class Meta:
        model = ContractLable
        fields = '__all__'


class ContractFolderSerializer(serializers.ModelSerializer):
    """Serializer class for ContractFolder model."""
    class Meta:
        model = ContractFolder
        fields = '__all__'
