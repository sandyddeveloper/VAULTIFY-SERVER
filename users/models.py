from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=120, blank=False)
    city = models.CharField(max_length=30, blank=False)
    postal_code = models.CharField(max_length=6, blank=False)
    date_of_birth = models.DateField(blank=False)
    pancard = models.CharField(max_length=50, blank=False)
    dwolla_customer_url = models.URLField(max_length=2000, blank=False)
    dwolla_customer_id = models.CharField(max_length=200, blank=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "date_of_birth"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
