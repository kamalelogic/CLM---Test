from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from contract_review_approval import serializer
from contract_review_approval.models import ContractActivityLog, ContractApprover, ContractMetadata, ContractReviewer, Metadata

# Create your views here.

################################################################
########################   ContractReviewer    #################
################################################################

# ListView


class ContractReviewerListView(generics.ListAPIView):

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# OneView


class ContractReviewerOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# CreateView


class ContractReviewerCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# UpdateView


class ContractReviewerUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# DeleteView


class ContractReviewerDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()


# Contract Reviewers By ContractView

class ContractReviewersByContractView(generics.ListAPIView):
    serializer_class = serializer.ContractReviewerSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractReviewer.objects.filter(contract_id=contract_id)

################################################################
########################   ContractActivityLog    ##############
################################################################

# ListView


class ContractActivityLogListView(generics.ListAPIView):

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# OneView


class ContractActivityLogOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# CreateView


class ContractActivityLogCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# UpdateView


class ContractActivityLogUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# DeleteView


class ContractActivityLogDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()


################################################################
########################   ContractApprover    #################
################################################################

# ListView
class ContractApproverListView(generics.ListAPIView):

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

# OneView


class ContractApproverOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

# CreateView


class ContractApproverCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

# UpdateView


class ContractApproverUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

# DeleteView


class ContractApproverDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()


# Contract Approvers By ContractView


class ContractApproversByContractView(generics.ListAPIView):
    serializer_class = serializer.ContractApproverSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractApprover.objects.filter(contract_id=contract_id)


################################################################
########################   Metadata    #########################
################################################################

# ListView
class MetadataListView(generics.ListAPIView):

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# OneView


class MetadataOneView(generics.RetrieveAPIView):

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# CreateView


class MetadataCreateView(generics.CreateAPIView):

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# UpdateView


class MetadataUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# DeleteView


class MetadataDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()


################################################################
########################   ContractMetadata    #################
################################################################

# ListView
class ContractMetadataListView(generics.ListAPIView):

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# OneView


class ContractMetadataOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# CreateView


class ContractMetadataCreateView(generics.CreateAPIView):

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# UpdateView


class ContractMetadataUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# DeleteView


class ContractMetadataDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

########################################################################


class CreateAdditionalMetaTagView(generics.CreateAPIView):
    serializer_class = serializer.MetadataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class AddAdditionalMetaTagToContractView(generics.CreateAPIView):
    serializer_class = serializer.ContractMetadataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
