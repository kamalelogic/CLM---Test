from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import ContractReviewer, ContractActivityLog, ContractApprover, ContractMetadata,  Metadata

# ContractReviewer


class ContractReviewerForm(forms.ModelForm):
    class Meta:
        model = ContractReviewer
        fields = '__all__'


class ContractReviewerAdmin(admin.ModelAdmin):
    form = ContractReviewerForm


admin.site.register(ContractReviewer, ContractReviewerAdmin)


# ContractActivityLog

class ContractActivityLogForm(forms.ModelForm):
    class Meta:
        model = ContractActivityLog
        fields = '__all__'


class ContractActivityLogAdmin(admin.ModelAdmin):
    form = ContractActivityLogForm


admin.site.register(ContractActivityLog, ContractActivityLogAdmin)

# ContractApprover


class ContractApproverForm(forms.ModelForm):
    class Meta:
        model = ContractApprover
        fields = '__all__'


class ContractApproverAdmin(admin.ModelAdmin):
    form = ContractApproverForm


admin.site.register(ContractApprover, ContractApproverAdmin)


# Metadata

class MetadataForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = '__all__'


class MetadataAdmin(admin.ModelAdmin):
    form = MetadataForm


admin.site.register(Metadata, MetadataAdmin)

# ContractMetadata


class ContractMetadataForm(forms.ModelForm):
    class Meta:
        model = ContractMetadata
        fields = '__all__'


class ContractMetadataAdmin(admin.ModelAdmin):
    form = ContractMetadataForm


admin.site.register(ContractMetadata, ContractMetadataAdmin)
