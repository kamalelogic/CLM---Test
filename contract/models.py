from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from customer_and_user_management.models import User
from counterparty.models import Counterparty

######################################################################
######################### ContractTemplate ###########################
######################################################################


class ContractTemplate(models.Model):
    """Model representing a contract template."""
    contract_template_id = models.AutoField(primary_key=True, null=False)
    contract_template_name = models.CharField(max_length=50)
    contract_template_doc_file_path = models.TextField()
    qa_template_file_path = models.TextField()
    contract_type = models.ForeignKey('ContractType', on_delete=models.CASCADE)
    created_at = models.DateTimeField(name=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        """Returns a string representation of the Contract object."""
        return self.contract_template_name

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.contract_template_name:
            raise ValidationError('contract_template_name is required.')
        if not self.contract_template_doc_file_path:
            raise ValidationError(
                'Contract template doc file path is required.')
        if not self.qa_template_file_path:
            raise ValidationError('Qa template file path is required.')

    class Meta:
        verbose_name_plural = "1. ContractTemplate"

########################################################################
########################## ContractType ################################
########################################################################


class ContractType(models.Model):
    """Model representing a contract type."""
    contract_type_id = models.AutoField(primary_key=True)
    contract_type = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def clean(self):
        if not self.contract_type:
            raise ValidationError('contract type is required.')

    def __str__(self):
        return self.contract_type

    class Meta:
        verbose_name_plural = "2. ContractType"

#############################################################################
########################### ContractStatus ##################################
#############################################################################


class ContractStatus(models.Model):
    """Model representing a Contract Status."""
    contract_status_id = models.AutoField(primary_key=True)
    contract_status = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.contract_status:
            raise ValidationError('Contract Status is required.')

    class Meta:
        verbose_name_plural = "8. ContractStates"

########################################################################
######################## ContractAttachment ############################
########################################################################


class ContractAttachment(models.Model):
    """Model representing a contract attachment."""
    contract_attachment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.TextField()
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE)
    attachment_name = models.CharField(max_length=50)
    uploaded_date = models.DateTimeField()

    def __str__(self):
        """Returns a string representation of the Attachment object."""
        return self.attachment_name

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.file_path:
            raise ValidationError('File Path is required.')
        if not self.attachment_name:
            raise ValidationError('Attachment Name type is required.')
        if not self.attachment_name:
            raise ValidationError('Uploaded date  is required.')

    class Meta:
        verbose_name_plural = "3. ContractAttachment"

#########################################################################
############################### Contract ################################
#########################################################################


class Contract(models.Model):
    """Model representing a contract."""
    contract_id = models.AutoField(primary_key=True)
    contract_status = models.ForeignKey(
        'ContractStatus', on_delete=models.CASCADE)
    customer = models.ForeignKey(
        'customer_and_user_management.Customer', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    contract_manager = models.ForeignKey(
        User, related_name='contract_manager', on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()
    signed_date = models.DateTimeField()
    last_updated_date = models.DateTimeField()
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    contract_industry = models.CharField(max_length=255)
    contract_document_path = models.TextField()
    qa_template_file_path = models.TextField()
    # contract_status_id = models.ForeignKey(ContractStatus, related_name='contract_statuses', on_delete=models.CASCADE)
    contract_template = models.ForeignKey(
        ContractTemplate, on_delete=models.CASCADE)
    contract_uploaded_source = models.CharField(max_length=12)
    meta_tag_document_path = models.TextField()
    contract_name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        """Returns a string representation of the Contract object."""
        return self.contract_name

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.contract_document_path:
            raise ValidationError('Contract document path is required.')
        if not self.qa_template_file_path:
            raise ValidationError('QA template file path is required.')
        if not self.contract_name:
            raise ValidationError('contract_name  is required.')
        if not self.created_at:
            raise ValidationError('Created_at  is required.')
        if not self.updated_at:
            raise ValidationError('Updated at  is required.')

    class Meta:
        verbose_name_plural = "4. Contract"

##########################################################################
############################# ContractAuthor #############################
##########################################################################


class ContractAuthor(models.Model):
    """Model representing a contract author."""
    contract_author_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    status = models.BooleanField()
    remarks = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = "5. ContractAuthor"

###########################################################################
###################### ContractCounterparty ###############################
###########################################################################


class ContractCounterparty(models.Model):
    """Model representing a contract counterparty."""
    contract_counterparty_id = models.AutoField(primary_key=True)
    counterparty = models.ForeignKey(Counterparty, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = "6. ContractCounterparty"

#############################################################################
############################ Country ########################################
#############################################################################


class Country(models.Model):
    """Model representing a country."""
    country_id = models.AutoField(primary_key=True, null=False)
    country_name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the object."""
        return self.country_name

    def clean(self):
        """Performs model validation and raises ValidationError if any validation fails."""
        if not self.country_name:
            raise ValidationError('Country name is required.')
        if self.status not in [True, False]:
            raise ValidationError(
                'Invalid status value. Status must be either True or False.')

    class Meta:
        verbose_name_plural = "7. Country"


#############################################################################
########################## ContractHistory ##################################
#############################################################################


class ContractHistory(models.Model):
    """Model representing a Contract History."""
    contract_history_id = models.AutoField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=5)
    contract_document_path = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    qa_template_file_path = models.TextField()

    def clean(self):
        if not self.version_number:
            raise ValidationError('version_number  is required.')
        if not self.contract_document_path:
            raise ValidationError('Contract document path  is required.')
        if not self.version_number:
            raise ValidationError('version_number  is required.')
        if not self.qa_template_file_path:
            raise ValidationError('QA template file path  is required.')

    class Meta:
        verbose_name_plural = "9. ContractHistory"
