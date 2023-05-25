from django.shortcuts import render

from contract_renew import serializer
from contract_renew.models import RenewContract, UploadContract, UploadedContractStatus
from rest_framework import generics


# Create your views here.

################################################################
########################   UploadContract    ###################
################################################################

# ListView
class UploadContractListView(generics.ListAPIView):

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# OneView


class UploadContractOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# CreateView


class UploadContractCreateView(generics.CreateAPIView):

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# UpdateView


class UploadContractUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# DeleteView


class UploadContractDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()


################################################################
########################   RenewContract    ####################
################################################################

# ListView
class RenewContractListView(generics.ListAPIView):

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# OneView


class RenewContractOneView(generics.RetrieveAPIView):

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# CreateView


class RenewContractCreateView(generics.CreateAPIView):

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# UpdateView


class RenewContractUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# DeleteView


class RenewContractDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()


################################################################
########################   UploadedContractStatus    ###########
################################################################

# ListView
class UploadedContractStatusListView(generics.ListAPIView):

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# OneView


class UploadedContractStatusOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# CreateView


class UploadedContractStatusCreateView(generics.CreateAPIView):

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# UpdateView


class UploadedContractStatusUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# DeleteView


class UploadedContractStatusDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()
