from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Company")
    activity = models.BooleanField(default=True, verbose_name="Аctivity")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company"


class ConfigData(models.Model):
    company = models.ForeignKey("Company", blank=False, verbose_name='Company', on_delete=models.CASCADE)
    param_key = models.CharField(max_length=200, verbose_name="Param key")
    param_val = models.TextField(blank=True, verbose_name="Date end of action")

    class Meta:
        verbose_name = "Config data"
        verbose_name_plural = "Config"