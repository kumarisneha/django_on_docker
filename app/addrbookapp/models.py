# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Address(models.Model):
    user = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100) 
    email_id = models.EmailField(max_length = 50, unique=True)
    phone_number = models.CharField(_('number'), max_length=10 ,unique=True)

    def __str__(self):
        return self.user
