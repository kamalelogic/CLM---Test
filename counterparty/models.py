from django.db import models

from customer_and_user_management.models import User, Customer
########################################################################
########################### Countryparty ###############################
########################################################################


class Counterparty(models.Model):
    """Model representing a counterparty."""
    counterparty_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    company_web = models.CharField(max_length=100)
    company_address = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    company_contact_number = models.CharField(max_length=14)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.company_name

########################################################################
##################### CustomerCounterpartyContract #####################
########################################################################


class CustomerCounterpartyContact(models.Model):
    """Model representing a customer counterparty contract."""
    customer_counterparty_contact_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    counterparty_contact_id = models.ForeignKey(
        'CounterpartyContact', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

#######################################################################
###################### CounterpartyContract ###########################
#######################################################################


class CounterpartyContact(models.Model):
    """Model representing a contact for a counterparty."""
    counterparty_contact_id = models.AutoField(primary_key=True)
    counterparty_id = models.ForeignKey(Counterparty, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
