from django.db import models
from django.contrib import auth
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return '@{}'.format(self.username)

# class SignUpModel(models.Model):
#     username = models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     email = models.CharField(max_length=200)
#     password = models.TextField()
#     password2 = models.DateTimeField(default=timezone.now)
#     address = models.DateTimeField(blank=True,null=True)
