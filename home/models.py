from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
import uuid
from embed_video.fields import EmbedVideoField


class CustomerManager(BaseUserManager):
    def create_user(self, userEmail, first_name, last_name,
                    password = None,
                    is_admin = False,
                    is_staff = False,
                    is_active = True):
        if not userEmail:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a First Name")
        if not last_name:
            raise ValueError("User must have a Last Name")

        user = self.model(userEmail=self.normalize_email(userEmail))
        user.first_name = first_name
        user.last_name = last_name
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.set_password(password)
        user.save(using=self._db)

    def create_staffuser(self, userEmail, first_name, last_name,
                         password = None,):
        user = self.create_user(userEmail, first_name, last_name,
                                password, is_staff = True,)
        return user

    def create_superuser(self, userEmail, first_name, last_name,
                         password = None, **kwargs):
        if not userEmail:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a First Name")
        if not last_name:
            raise ValueError("User must have a Last Name")
        user = self.model(userEmail = self.normalize_email(userEmail))
        user.first_name = first_name
        user.last_name = last_name
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    userID = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    userEmail = models.EmailField(unique=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    objects = CustomerManager()
    is_active = models.BooleanField(default=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)
    USERNAME_FIELD = 'userEmail'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def userName(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        # The user is identified by their email address
        return self.userName

    def get_short_name(self):
        return self.first_name

    def get_user_id(self):
        return self.userID

    @staticmethod
    def has_perm(perm, obj = None ):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.userName

    class Meta:
        verbose_name_plural = "User"


class VideoItem(models.Model):
    url = EmbedVideoField()  # same like models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
