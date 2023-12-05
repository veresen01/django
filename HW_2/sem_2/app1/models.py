from random import choice

from django.db import models

CHOICES=('HEAD','TAIL')

class HeadTails(models.Model):
    side=models.CharField(max_length=4,default=choice(CHOICES))
    
