
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# from master_data.models import Currency, Language

# #########################################################################
# ############################## Permission ###############################
# #########################################################################

# class Permission(models.Model):
#     permission_id = models.AutoField(primary_key=True)
#     permission = models.CharField(max_length=255)
#     status = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.permission

# ##########################################################################
# ################################ UserManager #############################
# ##########################################################################

# class UserManager(BaseUserManager):
#     def create_user(self, first_name, last_name, username, email, password=None):
#         if not email:
#             raise ValueError('User must have an email address')
#         if not username:
#             raise ValueError('User must have an username')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, first_name, last_name, username, email, password=None):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.is_superadmin = True
#         user.save(using=self._db)
#         return user

# #########################################################################
# ############################### User ####################################
# #########################################################################

# class User(AbstractBaseUser):
#     ContractManager = 1
#     ContractAuthor = 2
#     ContractReviewer = 3
#     ContractApprover = 4
#     ExternalContractReviewers = 5
#     ExternalContractApprovers = 6
#     TaskAuthors = 7
#     AnalyticsMgr = 8
#     UserAdmin = 9
#     OrgAdmin = 10

#     ROLE_CHOICES = (
#         (ContractManager, 'ContractManager'),
#         (ContractAuthor, 'ContractAuthor'),
#         (ContractReviewer, 'ContractReviewer'),
#         (ContractApprover, 'ContractApprover'),
#         (ExternalContractReviewers, 'ExternalContractReviewers'),
#         (ExternalContractApprovers, 'ExternalContractApprovers'),
#         (TaskAuthors, 'TaskAuthors'),
#         (AnalyticsMgr, 'AnalyticsMgr'),
#         (UserAdmin, 'UserAdmin'),
#         (OrgAdmin, 'OrgAdmin'),
#     )
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=58)
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     phone_number = models.CharField(max_length=12, blank=True)
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

#     # required fields
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now_add=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_superadmin = models.BooleanField(default=False)
#     status = models.BooleanField(default=True)
#     permissions = models.ManyToManyField(Permission, through='UserPermission')


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ["username", 'first_name', "last_name"]

#     objects = UserManager()


#     def __str__(self):
#           return self.email

#     def has_perm(self, perm, obj=None):
#           return self.is_admin

#     def has_module_perms(self, app_label):
#           return True

# #######################################################################
# ################################ Country ##############################
# #######################################################################

# class Country(models.Model):
#     country_id = models.AutoField(primary_key=True)
#     country = models.CharField(max_length=30)
#     status = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# ########################################################################
# ############################## Customer ################################
# ########################################################################

# class Customer(models.Model):
#     customer_id = models.AutoField(primary_key=True)
#     company_url = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=200)
#     company_address = models.CharField(max_length=500)
#     contact_number = models.CharField(max_length=14)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     gst_tax_number = models.CharField(max_length=10)
#     company_logo_url = models.CharField(max_length=100)
#     company_image = models.ImageField(upload_to='company_images/')
#     contact_name = models.CharField(max_length=200)
#     contact_email = models.EmailField(max_length=50)
#     contact_phone_number = models.CharField(max_length=14)
#     licence_type = models.CharField(max_length=8)
#     licence_start_date = models.DateField()
#     licence_end_date = models.DateField()
#     licence_user_quantity = models.IntegerField()
#     status = models.BooleanField(default=True)
#     is_social_login_enabled = models.BooleanField(default=False)
#     unique_id = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     org_admin_email = models.EmailField(max_length=50)
#     org_admin_full_name = models.CharField(max_length=100)
#     org_admin_contact_number = models.CharField(max_length=14)
#     contract_manager_email = models.EmailField(max_length=50)
#     contract_manager_full_name = models.CharField(max_length=100)
#     contract_manager_contact_number = models.CharField(max_length=14)

# #########################################################################
# ############################## UserProfile ##############################
# #########################################################################

# class UserProfile(models.Model):
#     user_profile_id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_profile')
#     # customer = models.ForeignKey(Customer, on_delete=models.deletion.CASCADE, related_name='user_profiles')
#     # ... rest of your fields and methods ...

#     # profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
#     # cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
#     address_line_1 = models.CharField(max_length=50, blank=True, null=True)
#     address_line_2 = models.CharField(max_length=50, blank=True, null=True)
#     country = models.CharField(max_length=15, blank=True, null=True)
#     state = models.CharField(max_length=15, blank=True, null=True)
#     city = models.CharField(max_length=15, blank=True, null=True)
#     pin_code = models.CharField(max_length=6, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     language = models.ForeignKey(Language, on_delete=models.CASCADE) # Assuming 1 is the primary key of Language model
#     currency = models.ForeignKey(Currency, on_delete=models.CASCADE) # Assuming 1 is the primary key of Currency model
#     # date_formate = models.ForeignKey(DateFormate, on_delete=models.CASCADE, default=1) # Assuming 1 is the primary key of DateFormat model


#     def __str__(self):
#         return self.user.email

# #########################################################################
# ############################# UserPermission ############################
# #########################################################################


# class UserPermission(models.Model):
#     user_permission_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.user.username} - {self.permission.permission}'

# ###########################################################################
# ################################ Group ####################################
# ###########################################################################

# class Group(models.Model):
#     group_id = models.AutoField(primary_key=True)
#     group_name = models.CharField(max_length=200)
#     description = models.TextField()
#     status = models.BooleanField(default=True)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# ############################################################################
# ############################# UserProfileGroup #############################
# ############################################################################

# class UserProfileGroup(models.Model):
#     user_profile_group_id = models.AutoField(primary_key=True)
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     status = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_group_lead = models.BooleanField(default=False)

# # class GroupRole(models.Model):
# #     group_role_id = models.AutoField(primary_key=True)
# #     group = models.ForeignKey(Group, on_delete=models.CASCADE)
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     status = models.BooleanField(default=True)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from master_data.models import Currency, Language, DateFormat
from django_rest_passwordreset.signals import reset_password_token_created

#  sending emails to password tokn


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

# end


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True, null=False)
    permission = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.permission:
            raise ValidationError('Plese write valid permisson name.')
        if self.status not in [True, False]:
            raise ValidationError(
                'Invalid status value. Status must be either True or False.')

    def __str__(self):
        return self.permission


class Role(models.Model):
    ROLE_CHOICES = (
        ('ContractManager', 'ContractManager'),
        ('ContractAuthor', 'ContractAuthor'),
        ('ContractReviewer', 'ContractReviewer'),
        ('ContractApprover', 'ContractApprover'),
        ('ExternalContractReviewers', 'ExternalContractReviewers'),
        ('ExternalContractApprovers', 'ExternalContractApprovers'),
        ('TaskAuthors', 'TaskAuthors'),
        ('AnalyticsMgr', 'AnalyticsMgr'),
        ('UserAdmin', 'UserAdmin'),
        ('OrgAdmin', 'OrgAdmin'),
    )

    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, choices=ROLE_CHOICES)
    description = models.TextField()
    status = models.BooleanField(default=True)
    customer_id = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):

        if self.status not in [True, False]:
            raise ValidationError(
                'Invalid status value. Status must be either True or False.')
        if self.created_at and self.created_at >= timezone.now():
            raise ValidationError('Created at date cannot be in the future.')

    def __str__(self):
        return self.role_name


class RolePermission(models.Model):
    role_permission_id = models.AutoField(primary_key=True, null=False)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)
    permission_id = models.ForeignKey(
        Permission, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.role_permission_id


# class User(AbstractBaseUser):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=12)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=12)
#     status = models.BooleanField(default=False)
#     customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     contact_phone_number = models.CharField(max_length=14)
#     department = models.CharField(max_length=50)
#     language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
#     currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
#     date_format_id = models.ForeignKey(DateFormat, on_delete=models.CASCADE)
#     password_reset_token = models.CharField(max_length=100)
#     password_reset_token_sent_at = models.DateTimeField()
#     updated_at = models.DateTimeField(auto_now=True)
#     groups = models.ManyToManyField('Group')
#     roles = models.ManyToManyField(Role, through='UserRole')
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name='user permissions',
#         blank=True,
#         related_name='customer_and_user_permissions'
#     )
# 33333333333333333333333333333333333333333333333333333333333


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    status = models.BooleanField(default=False)
    customer_id = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True)
    contact_phone_number = models.CharField(max_length=14, null=True)
    department = models.CharField(max_length=50, null=True)
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, null=True)
    date_format_id = models.ForeignKey(
        DateFormat, on_delete=models.CASCADE, null=True)
    password_reset_token = models.CharField(max_length=100)
    password_reset_token_sent_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField('Group', null=True)
    roles = models.ManyToManyField(Role, through='UserRole', null=True)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customer_and_user_permissions', null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    ############################################################################

    # def clean(self):
    #     if not self.email:
    #         raise ValidationError('Email is required.')
    #     if not self.password:
    #         raise ValidationError('Password is required.')
    #     if not self.first_name:
    #         raise ValidationError('First name is required.')

    # def __str__(self):
    #     return self.first_name


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.user_role_id


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.country:
            raise ValidationError('Country is required.')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = "Countries"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    company_url = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=14)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gst_tax_number = models.CharField(max_length=10)
    company_logo_url = models.CharField(max_length=100)
    company_image = models.ImageField(upload_to='company_images/')
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=50)
    contact_phone_number = models.CharField(max_length=14)
    licence_type = models.CharField(max_length=8)
    licence_start_date = models.DateField()
    licence_end_date = models.DateField()
    licence_user_quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    is_social_login_enabled = models.BooleanField(default=False)
    unique_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    org_admin_email = models.EmailField(max_length=50)
    org_admin_full_name = models.CharField(max_length=100)
    org_admin_contact_number = models.CharField(max_length=14)
    contract_manager_email = models.EmailField(max_length=50)
    contract_manager_full_name = models.CharField(max_length=100)
    contract_manager_contact_number = models.CharField(max_length=14)

    def clean(self):
        if not self.company_url:
            raise ValidationError('company url is required.')
        if not self.company_name:
            raise ValidationError('Company name is required.')
        if not self.licence_type:
            raise ValidationError('licence type is required.')
        if not self.licence_start_date:
            raise ValidationError('licence start date is required.')
        if not self.licence_end_date:
            raise ValidationError('licence end date is required.')
        if not self.licence_user_quantity:
            raise ValidationError('licence user quantity is required.')

    def __str__(self):
        return self.company_name


class Group(models.Model):
    group_id = models.AutoField(primary_key=True, null=False)
    group_name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    status = models.BooleanField(null=False)
    customer_id = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.group_name:
            raise ValidationError('Group Name  is required.')

    def __str__(self):
        return self.group_name


class GroupRole(models.Model):
    group_role_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.BooleanField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_group_lead = models.BooleanField(null=False)


class UserGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, null=False)
    status = models.BooleanField(null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField()
    is_group_lead = models.BooleanField()

    def clean(self):
        if self.created_at and self.created_at >= timezone.now():
            raise ValidationError('Created at date cannot be in the future.')
