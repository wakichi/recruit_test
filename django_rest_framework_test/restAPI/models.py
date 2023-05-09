from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class User(models.Model):
    # userid, pass, nick, comment
    user_id = models.CharField(primary_key=True,max_length=20,validators=[MinLengthValidator(6)])
    password = models.CharField(max_length=20,validators=[MinLengthValidator(8)])
    nickname = models.CharField(max_length=30, blank =True, null =True)
    comment = models.CharField(max_length=100, blank =True, null =True)