from django.db import models

# Create your models here.
from django.contrib.auth.models import UserManager, AbstractUser

class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        # create_user と create_superuser の共通処理
        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):

        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)
        
class CustomUser(AbstractUser): 
    objects = CustomUserManager()

    sex = models.CharField(verbose_name="性別", max_length=1, choices=[(None, "--"), ("0", "男性"), ("1", "女性")], default=None, blank=True, null=True)
    age = models.CharField(verbose_name="年代", max_length=1, choices=[(None, "--"), ("1", "10代"), ("2", "20代"), ("3", "30代"), ("4", "40代"), ("5", "50代")], default=None, blank=True, null=True)

    REQUIRED_FIELDS = ["email", "sex", "age"]

    def __str__(self):
        return self.username