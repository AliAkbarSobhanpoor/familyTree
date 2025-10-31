from django.db import models
from filer.fields.image import FilerImageField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Person(models.Model):
    """
    Represents a person in the family tree.
    """
    first_name = models.CharField(verbose_name="نام", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=100, blank=True, null=True)
    description = models.TextField(verbose_name="توضیحات", blank=True, null=True)
    avatar = FilerImageField(verbose_name="آواتار", blank=True, null=True, on_delete=models.SET_NULL)


    GENDER_CHOICES = [
        ('M', 'مرد'),
        ('F', 'زن'),
    ]
    gender = models.CharField(verbose_name="جنسیت", max_length=1, choices=GENDER_CHOICES)

    spouses = models.ManyToManyField('self',verbose_name="همسران", symmetrical=True, blank=True, related_name='spouse_of')
    parents = models.ManyToManyField('self', verbose_name="والدین", symmetrical=False, blank=True, related_name='children_of')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    class Meta:
        verbose_name = "شخص"
        verbose_name_plural = "افراد"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"