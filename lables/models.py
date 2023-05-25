from django.db import models

# Create your models here.
from contract.models import Contract

from customer_and_user_management.models import Customer, User

###############################################################
########################## LabelMaster ########################
###############################################################


class LabelMaster(models.Model):
    """Model class representing a label master."""
    label_master_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "1. LabelMaster"

#################################################################
########################  ContractLable #########################
#################################################################

# ContractLable


class ContractLable(models.Model):
    """Model class representing a Contract Lable."""
    contract_lable_id = models.AutoField(primary_key=True)
    status = models.BooleanField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = "2. ContractLable"

##################################################################
######################## ContractFolder ##########################
##################################################################

# ContractFolder


class ContractFolder(models.Model):
    """Model class representing a Contract Folder."""
    Contract_folder_id = models.AutoField(primary_key=True)
    folder_namel = models.CharField(max_length=50)
    status = models.BooleanField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.folder_namel

    class Meta:
        verbose_name_plural = "3. ContractFolder"
