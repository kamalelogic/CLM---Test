from customer_and_user_management.models import Country, Customer, Group, Permission, User, Role, RolePermission, UserRole, GroupRole, UserGroup
from rest_framework import serializers
from rest_framework import generics
from rest_framework.response import Response


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for the password change endpoint.

    This serializer defines the fields required for changing a user's password.

    Fields:
        old_password (str): The old password.
        new_password (str): The new password.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# User loging logout and profile Serilize


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
# End of the User create update and profile serializer


class PermissionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Permission model.
    """
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Role model.
    """
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for the Country model.
    """
    class Meta:
        model = Country
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
    """
    class Meta:
        model = Customer
        fields = '__all__'


class RolePermissionSerializer(serializers.ModelSerializer):
    """
    Serializer for the RolePermission model.
    """
    class Meta:
        model = RolePermission
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserRole model.
    """
    class Meta:
        model = UserRole
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model.
    """
    class Meta:
        model = Group
        fields = '__all__'


class GroupRoleSerializer(serializers.ModelSerializer):
    """
    Serializer for the GroupRole model.
    """
    class Meta:
        model = GroupRole
        fields = '__all__'


class UserGroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserGroup model.
    """
    class Meta:
        model = UserGroup
        fields = ['user_group_id', 'user_id', 'group_id',
                  'status', 'created_at', 'updated_at', 'is_group_lead']
