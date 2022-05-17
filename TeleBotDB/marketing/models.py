from django.db import models
from users.models import *


# Create your models here.
class Promotions(models.Model):
    date_start = models.DateTimeField(auto_now_add=False, verbose_name="Date beginning of the action")
    date_end = models.DateTimeField(auto_now_add=False, verbose_name="Date end of action")
    description = models.TextField(blank=False, verbose_name="Description")
    activity = models.BooleanField(default=True, verbose_name="Аctivity")
    image_url = models.CharField(max_length=255, blank=True, verbose_name="Image URL")
    data_sync = models.DateTimeField(auto_now_add=True, verbose_name="Sync date with other app")
    company = models.ForeignKey(Company, blank=False, verbose_name='Company', on_delete=models.CASCADE)
    guid_one_c = models.CharField(max_length=36, blank=False, verbose_name="1C GUID", unique=True, default="")

    def __str__(self):
        return "Marketing Promotions"

    class Meta:
        verbose_name = "Marketing promotion"
        verbose_name_plural = "Marketing promotions"


class Bonuses(models.Model):
    quantity = models.IntegerField(verbose_name="Number of points")
    user = models.ForeignKey(Users, blank=False, verbose_name='Users', on_delete=models.CASCADE)
    data_sync = models.DateTimeField(auto_now_add=True, verbose_name="Sync date with other app")

    def __str__(self):
        return "Bonuses"

    class Meta:
        verbose_name = "Bonus"
        verbose_name_plural = "Bonuses"
