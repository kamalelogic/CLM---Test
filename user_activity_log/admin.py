from django import forms
from django.contrib import admin

# Register your models here.

from .models import (
    UserActivityLog, AnalyticalReportList, ReportDeliverySchedule,
    ReportDeliveryLog, EmailDeliveryLog, SmsDeliveryLog
)

# UserActivityLog


class UserActivityLogForm(forms.ModelForm):
    """Form for the UserActivityLog model."""
    class Meta:
        model = UserActivityLog
        fields = '__all__'


class UserActivityLogAdmin(admin.ModelAdmin):
    form = UserActivityLogForm


admin.site.register(UserActivityLog, UserActivityLogAdmin)

# AnalyticalReportList


class AnalyticalReportListForm(forms.ModelForm):
    """Form for the AnalyticalReportList model."""
    class Meta:
        model = AnalyticalReportList
        fields = '__all__'


class AnalyticalReportListAdmin(admin.ModelAdmin):
    form = AnalyticalReportListForm


admin.site.register(AnalyticalReportList, AnalyticalReportListAdmin)

# ReportDeliverySchedule


class ReportDeliveryScheduleForm(forms.ModelForm):
    """Form for the ReportDeliverySchedule model."""
    class Meta:
        model = ReportDeliverySchedule
        fields = '__all__'


class ReportDeliveryScheduleAdmin(admin.ModelAdmin):
    form = ReportDeliveryScheduleForm


admin.site.register(ReportDeliverySchedule, ReportDeliveryScheduleAdmin)

# ReportDeliveryLog


class ReportDeliveryLogForm(forms.ModelForm):
    """Form for the ReportDeliveryLog model."""
    class Meta:
        model = ReportDeliveryLog
        fields = '__all__'


class ReportDeliveryLogAdmin(admin.ModelAdmin):
    form = ReportDeliveryLogForm


admin.site.register(ReportDeliveryLog, ReportDeliveryLogAdmin)

# EmailDeliveryLog


class EmailDeliveryLogForm(forms.ModelForm):
    """Form for the EmailDeliveryLog model."""
    class Meta:
        model = EmailDeliveryLog
        fields = '__all__'


class EmailDeliveryLogAdmin(admin.ModelAdmin):
    form = EmailDeliveryLogForm


admin.site.register(EmailDeliveryLog, EmailDeliveryLogAdmin)

# SmsDeliveryLog


class SmsDeliveryLogForm(forms.ModelForm):
    """Form for the SmsDeliveryLog model."""
    class Meta:
        model = SmsDeliveryLog
        fields = '__all__'


class SmsDeliveryLogAdmin(admin.ModelAdmin):
    form = SmsDeliveryLogForm


admin.site.register(SmsDeliveryLog, SmsDeliveryLogAdmin)
