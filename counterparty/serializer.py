from counterparty.models import (
    Counterparty, CounterpartyContact, CustomerCounterpartyContact
)
from rest_framework import serializers


class CountrypartySerializer(serializers.ModelSerializer):
    class Meta:
        """Serializer for the Counterparty model."""
        model = Counterparty
        fields = '__all__'


class CustomerCounterpartyContractSerializer(serializers.ModelSerializer):
    class Meta:
        """Serializer for the CustomerCounterpartyContact model."""
        model = CustomerCounterpartyContact
        fields = '__all__'


class CounterpartyContractSerializer(serializers.ModelSerializer):
    class Meta:
        """Serializer for the CounterpartyContact model."""
        model = CounterpartyContact
        fields = '__all__'
