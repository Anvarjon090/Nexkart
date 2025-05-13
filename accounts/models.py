from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import BaseModel
from accounts.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # email and password only

    def __str__(self):
        return self.email
    

class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.RESTRICT, null=True, blank=True)
    product = models.ForeignKey('products.ProductVariant', on_delete=models.RESTRICT, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"CartItem({self.id})"