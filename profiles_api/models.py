from django.db import models

# Inbuilt user model from Django
from django.contrib.auth.models import AbstractBaseUser

# PermissionsMixin is a mixin class that provides
# a set of methods and fields required by the PermissionRequiredMixin to
# handle user persmissions
from django.contrib.auth.models import PermissionsMixin

# BaseUserManager is a base class for user model managers
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # [set password] encrypts the password before saving it to the database
        user.set_password(password)
        user.save(using=self._db)  # saves to db

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system.
    :param AbstractBaseUser: Inbuilt user model from Django
    :PermissionsMixin: PermissionsMixin is a mixin class that provides
    a set of methods and fields require
    by the PermissionRequiredMixin to handle user persmissions.
    :return: name, email, password, is_active, is_staff, is_superuser
    """

    email = models.EmailField(max_length=255, unique=True)
    """gets the  user email"""
    # unique-is used to make sure that no two users can have the same email

    name = models.CharField(max_length=255)
    """ gets the user's name"""

    is_active = models.BooleanField(default=True)
    """ gets the active status,
    default true, but can be deactivated in future"""

    is_staff = models.BooleanField(default=False)
    """gets the active status,
    default true, but can be deactivated in future"""

    objects = UserProfileManager()

    USERNAME_FIELD = "email"  # takes the email as the username
    REQUIRED_FIELDS = ["name"]  # name is required

    def get_full_name(self):
        """Retrieve the users full name"""
        return self.name

    def get_short_name(self):
        """Retrieve the users short name"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
