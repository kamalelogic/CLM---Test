from rest_framework import serializers
from to_do_list.models import action_item_list


class action_item_listSerializer(serializers.ModelSerializer):
    """Serializer for the action_item_list model."""
    class Meta:
        model = action_item_list
        fields = '__all__'
