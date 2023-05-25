from django.db import models
from django.core.exceptions import ValidationError
from customer_and_user_management.models import User, Customer
from contract.models import Contract


######################################################################
######################### ContractReviewer ###########################
######################################################################

class ContractReviewer(models.Model):
    """Model representing a contract reviewer."""
    contract_reviewer_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review_status = models.IntegerField()
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    review_order = models.IntegerField()
    internal_or_external = models.CharField(max_length=10)
    remarks = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField()

#################### back-end validation shema ########################

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.review_status:
            raise ValidationError('Version number  is required.')
        if not self.review_order:
            raise ValidationError('Review order document path  is required.')
        if not self.internal_or_external:
            raise ValidationError('Internal or external  is required.')


######################################################################
######################### ContractActivityLog ########################
######################################################################

class ContractActivityLog(models.Model):
    """Model representing a contract activity log."""
    contract_activity_log_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    activity = models.CharField(max_length=255)
    activity_time = models.DateTimeField(null=False)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField()
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)

#################### back-end validation shema ########################

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.activity:
            raise ValidationError('Activity  is required.')
        if not self.activity_time:
            raise ValidationError('Activity time is required.')
        if not self.created_at:
            raise ValidationError('created at  is required.')


######################################################################
######################### ContractApprover ###########################
######################################################################

class ContractApprover(models.Model):
    """Model representing a Contract Approver log."""
    contract_approver_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    review_order = models.IntegerField()
    approve_status = models.IntegerField()
    internal_or_external = models.CharField(max_length=10)
    remarks = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

#################### back-end validation shema ########################

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.review_order:
            raise ValidationError('Review order  is required.')
        if not self.approve_status:
            raise ValidationError('Approve status  is required.')
        if not self.internal_or_external:
            raise ValidationError('Internal or external  is required.')
        if not self.created_at:
            raise ValidationError('Created at Date  is required.')

######################################################################
######################### ContractMetadata ###########################
######################################################################


class ContractMetadata(models.Model):
    """Model representing a Contract Metadata log."""
    contract_metadata_id = models.IntegerField(primary_key=True)
    metadata_id = models.ForeignKey('Metadata', on_delete=models.CASCADE)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    added_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    metadata_value = models.CharField(max_length=255)

#################### back-end validation shema ########################

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.created_at:
            raise ValidationError('Create Date is required.')


######################################################################
###################### Metadata ######################################
######################################################################

class Metadata(models.Model):
    """Model representing a Metadata log."""
    metadata_id = models.IntegerField(primary_key=True)
    metadata_key = models.CharField(max_length=20)
    created_date = models.DateTimeField(null=False)
    created_by_user_id = models.IntegerField(null=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#################### back-end validation shema ########################

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.metadata_key:
            raise ValidationError('Metadata key  is required.')
        if not self.created_date:
            raise ValidationError('Created date  is required.')
