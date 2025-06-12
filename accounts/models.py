from django.contrib.auth.models import AbstractUser

class Receptionist(AbstractUser):
    class Meta:
        verbose_name = 'Receptionist'
        verbose_name_plural = 'Receptionists'