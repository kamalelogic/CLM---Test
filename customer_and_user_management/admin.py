from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from .models import User, Permission, Country, Customer, Group, GroupRole, RolePermission, UserRole, Role, UserGroup


# Permission
class PermissionAdminForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('permission'):
            raise forms.ValidationError('Permission name is required.')
        if cleaned_data.get('status') not in [True, False]:
            raise forms.ValidationError(
                'Invalid status value. Status must be either True or False.')


class PermissionAdmin(admin.ModelAdmin):
    """
    Admin model for Permission.

    This class defines the admin interface for the Permission model.

    Attributes:
        form (PermissionAdminForm): The form to be used for Permission model.
    """
    form = PermissionAdminForm


admin.site.register(Permission, PermissionAdmin)


# Country
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class CountryAdmin(admin.ModelAdmin):
    """
    Admin model for Country.

    This class defines the admin interface for the Country model.

    Attributes:
        form (CountryForm): The form to be used for Country model.
    """
    form = CountryForm


admin.site.register(Country, CountryAdmin)


# User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(admin.ModelAdmin):
    """
    Admin model for User.

    This class defines the admin interface for the User model.

    Attributes:
        form (UserForm): The form to be used for User model.
    """
    form = UserForm


admin.site.register(User, UserAdmin)


# Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    """
    Admin model for Customer.

    This class defines the admin interface for the Customer model.

    Attributes:
        form (CustomerForm): The form to be used for Customer model.
    """
    form = CustomerForm


admin.site.register(Customer, CustomerAdmin)


# Group
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupAdmin(admin.ModelAdmin):
    """
    Admin model for Group.

    This class defines the admin interface for the Group model.

    Attributes:
        form (GroupForm): The form to be used for Group model.
    """
    form = GroupForm


admin.site.register(Group, GroupAdmin)
admin.site.register(Role)
admin.site.register(GroupRole)
admin.site.register(UserRole)
admin.site.register(RolePermission)


# UserGroup


class UserGroupForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = ['user_group_id', 'user_id', 'group_id',
                  'status', 'created_at', 'updated_at', 'is_group_lead']


class UserGroupAdmin(admin.ModelAdmin):
    """
    Admin model for UserGroup.

    This class defines the admin interface for the UserGroup model.

    Attributes:
        form (UserGroupForm): The form to be used for UserGroup model.
    """
    form = UserGroupForm


admin.site.register(UserGroup, UserGroupAdmin)
