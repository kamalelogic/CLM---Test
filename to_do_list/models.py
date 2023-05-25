from django.db import models
from contract.models import Contract

from customer_and_user_management.models import Customer, User

# Create your models here.

##########################################################################
######################### action_item_list ###############################
##########################################################################


class action_item_list(models.Model):
    """Model representing an action item in a to-do list."""
    action_item_id = models.AutoField(primary_key=True)
    action_name = models.CharField(max_length=200)
    action_description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    contract_id = models.ForeignKey(Contract,  on_delete=models.CASCADE)
    eta = models.DateTimeField()
    assigned_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_user_id = models.ForeignKey(UserProfile , on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    current_status = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.action_name
