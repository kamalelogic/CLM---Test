from django.shortcuts import render
from counterparty import serializer
import counterparty
from counterparty.models import Counterparty, CounterpartyContact, CustomerCounterpartyContact
from rest_framework import generics

# Create your views here.


################################################################
#######################   Counterparty    ######################
################################################################

# ListView
class CounterpartyListView(generics.ListAPIView):

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# OneView


class CounterpartyOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# CreateView


class CounterpartyCreateView(generics.CreateAPIView):

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# UpdateView


class CounterpartyUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# DeleteView


class CounterpartyDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# Counterparties By Customer View


class CounterpartiesByCustomerView(generics.ListAPIView):
    serializer_class = serializer.CountrypartySerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Counterparty.objects.filter(customer_id=customer_id)

################################################################
########################   CustomerCounterpartyContact    ######
################################################################

# ListView


class CustomerCounterpartyContactListView(generics.ListAPIView):

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# OneView


class CustomerCounterpartyContactOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# CreateView


class CustomerCounterpartyContactCreateView(generics.CreateAPIView):

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# UpdateView


class CustomerCounterpartyContactUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# DeleteView


class CustomerCounterpartyContactDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()


################################################################
#######################   CounterpartyContract    ##############
################################################################

# ListView
class CounterpartyContractListView(generics.ListAPIView):

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# OneView


class CounterpartyContractOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# CreateView


class CounterpartyContractCreateView(generics.CreateAPIView):

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# UpdateView


class CounterpartyContractUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# DeleteView


class CounterpartyContractDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()
