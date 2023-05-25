from rest_framework import serializers
from contract.models import ContractAttachment, ContractAuthor, ContractCounterparty, ContractHistory, ContractStatus, ContractTemplate, ContractType, Country, Contract

#############################################################################
###################### ContractTemplateSerializer ###########################
#############################################################################


class ContractTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractTemplate
        fields = '__all__'

#############################################################################
########################  ContractTypeSerializer ############################
#############################################################################


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = '__all__'

#############################################################################
#######################  ContractAttachmentSerializer #######################
#############################################################################


class ContractAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractAttachment
        fields = '__all__'

#############################################################################
#######################  Contract ###########################################
#############################################################################


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

#############################################################################
#######################  ContractAuthor #####################################
#############################################################################


class ContractAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractAuthor
        fields = '__all__'

#############################################################################
#######################  ContractCounterparty ###############################
#############################################################################


class ContractCounterpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractCounterparty
        fields = '__all__'

#############################################################################
########################## CountrySerializer ################################
#############################################################################


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

#############################################################################
#######################  ContractStatusSerializer ###########################
#############################################################################


class ContractStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractStatus
        fields = '__all__'

#############################################################################
###################### ContractHistorySerializer ############################
#############################################################################


class ContractHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractHistory
        fields = '__all__'

#############################################################################
######################### ContractSerializer ################################
#############################################################################


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
