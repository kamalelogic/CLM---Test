from django.contrib import admin

# Register your models here.


from .models import LabelMaster, ContractLable, ContractFolder

admin.site.register(LabelMaster)
admin.site.register(ContractLable)
admin.site.register(ContractFolder)
