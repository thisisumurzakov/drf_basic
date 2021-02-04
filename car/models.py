from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Car(models.Model):
    vin = models.CharField(verbose_name='Vin',db_index=True, unique=True, max_length=70)
    color = models.CharField(verbose_name='Color', max_length=70)
    brand = models.CharField(verbose_name='Brand', max_length=70)
    CAR_TYPES = (
        (1, 'Cobalt'),
        (2, 'Matiz'),
        (3, 'Spark'),
        (4, 'Jentra')
    )
    car_type = models.IntegerField(verbose_name='Car_type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)