from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email,name, password=None, **extra_fields):
        if not name:
            raise ValueError("User must have a Name")
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have an Password")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
 
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
            user = self.create_user(
                email=self.normalize_email(email),
                name=name,
                password=password,
            )
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user


class Account(AbstractBaseUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()

    def __str__(self):
        return f"{self.email}"

    def has_perm(self, perm, obj=None): 
        return True

    def has_module_perms(self, app_label):
        return True
    

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=50)
    address_line_1 = models.CharField(blank = True, max_length = 100)
    address_line_2 = models.CharField(blank = True, max_length = 100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
