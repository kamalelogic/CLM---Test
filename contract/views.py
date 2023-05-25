
from contract import serializer
from contract.models import Contract, ContractAttachment, ContractAuthor, ContractCounterparty, ContractHistory, ContractStatus, ContractTemplate, ContractType, Country
from rest_framework import generics
from django.shortcuts import render

# Create your views here.


################################################################
########################   ContractTemplate    #################
################################################################

# ListView
class ContractTemplateListView(generics.ListAPIView):

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# OneView


class ContractTemplateOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# CreateView


class ContractTemplateCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# UpdateView


class ContractTemplateUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# DeleteView


class ContractTemplateDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()


################################################################
#######################   ContractType    ######################
################################################################

# ListView
class ContractTypeListView(generics.ListAPIView):

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# OneView


class ContractTypeOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# CreateView


class ContractTypeCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# UpdateView


class ContractTypeUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# DeleteView


class ContractTypeDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()


################################################################
#######################   ContractAttachment    ################
################################################################

# ListView
class ContractAttachmentListView(generics.ListAPIView):

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()

# OneView


class ContractAttachmentOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()

# CreateView


class ContractAttachmentCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()

# UpdateView


class ContractAttachmentUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()

# DeleteView


class ContractAttachmentDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()


################################################################
#######################   Contract    ##########################
################################################################

# ListView
class ContractListView(generics.ListAPIView):

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# OneView


class ContractOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# CreateView


class ContractCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# UpdateView


class ContractUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# DeleteView


class ContractDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# Contract by status


class ContractsByStatusView(generics.ListAPIView):
    serializer_class = serializer.ContractSerializer

    def get_queryset(self):
        # Assuming you pass the status ID in the URL
        status_id = self.kwargs['status_id']
        return Contract.objects.filter(contract_status=status_id)

# ContractsByStatusAndCustomerView


class ContractsByStatusAndCustomerView(generics.ListAPIView):
    serializer_class = serializer.ContractSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        status_id = self.kwargs['status_id']
        return Contract.objects.filter(customer_id=customer_id, contract_status_id=status_id)

# ContractsByCustomerView


class ContractsByCustomerView(generics.ListAPIView):
    serializer_class = serializer.ContractSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Contract.objects.filter(customer_id=customer_id)

# ContractAuthorsByContractView


class ContractAuthorsByContractView(generics.ListAPIView):
    serializer_class = serializer.ContractAuthorSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractAuthor.objects.filter(contract_id=contract_id)

# Contract History


class ContractVersionsByContractView(generics.ListAPIView):
    serializer_class = serializer.ContractHistorySerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractHistory.objects.filter(contract_id=contract_id)

# Contract Attachment


class ContractAttachmentsByContractView(generics.ListAPIView):
    serializer_class = serializer.ContractAttachmentSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractAttachment.objects.filter(contract_id=contract_id)


################################################################
#######################   ContractAuthor    ####################
################################################################

# ListView
class ContractAuthorListView(generics.ListAPIView):

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# OneView


class ContractAuthorOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# CreateView


class ContractAuthorCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# UpdateView


class ContractAuthorUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# DeleteView


class ContractAuthorDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()


################################################################
#######################   ContractCounterparty    ##############
################################################################

# ListView
class ContractCounterpartyListView(generics.ListAPIView):

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# OneView


class ContractCounterpartyOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# CreateView


class ContractCounterpartyCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# UpdateView


class ContractCounterpartyUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# DeleteView


class ContractCounterpartyDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()


################################################################
#######################   Country    ###########################
################################################################

# ListView
class CountryListView(generics.ListAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# OneView


class CountryOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# CreateView


class CountryCreateView(generics.CreateAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# UpdateView


class CountryUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# DeleteView


class CountryDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()


################################################################
#######################   ContractStatus    ####################
################################################################

# ListView
class ContractStatusListView(generics.ListAPIView):

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# OneView


class ContractStatusOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# CreateView


class ContractStatusCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# UpdateView


class ContractStatusUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# DeleteView


class ContractStatusDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()


################################################################
#######################   ContractHistory    ####################
################################################################

# ListView
class ContractHistoryListView(generics.ListAPIView):

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# OneView


class ContractHistoryOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# CreateView


class ContractHistoryCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# UpdateView


class ContractHistoryUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# DeleteView


class ContractHistoryDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()
