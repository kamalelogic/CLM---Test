from http.client import ResponseNotReady
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
# from django.contrib.auth.models import User
from customer_and_user_management.models import User


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .serializer import UserSerializer


from customer_and_user_management import serializer
from customer_and_user_management.models import Country, Customer, Group, Permission, Role, RolePermission, UserRole, GroupRole, UserGroup
from .serializer import ChangePasswordSerializer

################################################################

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Views


@api_view()
@permission_classes([permissions.AllowAny])
def hello_world(request):
    return Response('Hello, World!')


class ChangePasswordView(generics.UpdateAPIView):
    """An endpoint for changing the password."""
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################################################################


# class ChangePasswordView(generics.UpdateAPIView):
#     """An endpoint for changing the password."""
#     serializer_class = ChangePasswordSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         return self.request.user

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }

#             return Response(response)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# password

# deactivate

class UserDeactivationView(APIView):
    @staticmethod
    def put(request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.is_active = False  # Deactivate the user
            user.save()
            return Response({'detail': 'User deactivated successfully.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
# Deactivate

#  User Looging logout and Profile


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'User logged out successfully'})


class UserProfileView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

#  End of the Use Loging logout  and Profile


class UserGroupAssignmentView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        group_id = request.data.get('group_id')
        try:
            user = self.queryset.get(pk=user_id)
            group = Group.objects.get(pk=group_id)
        except (User.DoesNotExist, Group.DoesNotExist):
            return Response(status=404)

        user.groups.add(group)
        user.save()
        return Response({'message': 'User assigned to group successfully'})


# Create your views here.

################################################################
#######################   Permission    ########################
################################################################

# ListView
class PermissionListView(generics.ListAPIView):

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# OneView


class PermissionOneView(generics.RetrieveAPIView):

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# CreateView


class PermissionCreateView(generics.CreateAPIView):

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# UpdateView


class PermissionUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# DeleteView


class PermissionDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()


################################################################
#######################   Role    ##############################
################################################################

# ListView
class RoleListView(generics.ListAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# OneView


class RoleOneView(generics.RetrieveAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# CreateView


class RoleCreateView(generics.CreateAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# UpdateView


class RoleUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# DeleteView


class RoleDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

################################################################
#######################   User    ##############################
################################################################

# ListView


class UserListView(generics.ListAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

# OneView


class UserOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

# CreateView


class UserCreateView(generics.CreateAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

# UpdateView


class UserUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

# DeleteView


class UserDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()


################################################################
#######################   Country    ###########################
################################################################

# ListView
class CountryListView(generics.ListAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# OneView


class CountryOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# CreateView


class CountryCreateView(generics.CreateAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# UpdateView


class CountryUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# DeleteView


class CountryDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()


################################################################
#######################   Customer    ##########################
################################################################

# ListView
class CustomerListView(generics.ListAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# OneView


class CustomerOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# CreateView


class CustomerCreateView(generics.CreateAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# UpdateView


class CustomerUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# DeleteView


class CustomerDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()


################################################################
#######################   RolePermission    ####################
################################################################

# ListView
class RolePermissionListView(generics.ListAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# OneView


class RolePermissionOneView(generics.RetrieveAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# CreateView


class RolePermissionCreateView(generics.CreateAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# UpdateView


class RolePermissionUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# DeleteView


class RolePermissionDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()


################################################################
#######################   UserRole    ##########################
################################################################

# ListView
class UserRoleListView(generics.ListAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# OneView


class UserRoleOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# CreateView


class UserRoleCreateView(generics.CreateAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# UpdateView


class UserRoleUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# DeleteView


class UserRoleDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()


################################################################
#######################   Group    #############################
################################################################

# ListView
class GroupListView(generics.ListAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# OneView


class GroupOneView(generics.RetrieveAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# CreateView


class GroupCreateView(generics.CreateAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# UpdateView


class GroupUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# DeleteView


class GroupDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()


################################################################
#######################   GroupRole    #########################
################################################################

# ListView
class GroupRoleListView(generics.ListAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# OneView


class GroupRoleOneView(generics.RetrieveAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# CreateView


class GroupRoleCreateView(generics.CreateAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# UpdateView


class GroupRoleUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# DeleteView


class GroupRoleDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

################################################################
#######################   UserGroup    #########################
################################################################

# ListView


class UserGroupListView(generics.ListAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# OneView


class UserGroupOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# CreateView


class UserGroupCreateView(generics.CreateAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# UpdateView


class UserGroupUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# DeleteView


class UserGroupDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()
