from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Create and save a SuperUser with the given email and password.
        """

        user = self.create_user(
            email=email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user


class Department(models.Model):
    """Department model class."""
    name = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    """Team model class."""
    name = models.CharField(max_length=30, blank=False, unique=True)
    department = models.ForeignKey(Department, related_name='organization', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return self.name


class Employee(AbstractBaseUser, PermissionsMixin):
    """Employee model class."""
    email = models.EmailField(blank=False, unique=True)
    department = models.OneToOneField(Department, related_name='employees', on_delete=models.CASCADE, blank=True,
                                      null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_leader = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return '{}'.format(self.email)
