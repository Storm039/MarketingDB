from django.db import models
from company.models import *


# {'IdTelegram': 774692386, 'Mention': '@Bogaychuk_A', 'FullName': 'Alexandr B.', 'UserName': 'Bogaychuk_A', 'Phone': ''}
class Users(models.Model):
    id_telegram = models.IntegerField(db_index=True, blank=False, verbose_name="Id Telegram")
    mention = models.CharField(max_length=200, verbose_name="Mention")
    full_name = models.CharField(blank=True, max_length=200, verbose_name="Full name")
    user_name = models.CharField(blank=True, default="", max_length=200, verbose_name="User name")
    phone = models.CharField(blank=True, max_length=50, verbose_name="Phone")
    company = models.ForeignKey(Company, blank=False, verbose_name='Company', on_delete=models.CASCADE)
    activity = models.BooleanField(default=True, verbose_name="Аctivity")
    approval = models.BooleanField(default=False, verbose_name="Approval to the processing of personal data")
    create_1c = models.BooleanField(default=False, verbose_name="Created in the 1C program")

    def __str__(self):
        return f'{self.user_name}, {self.full_name}, {self.phone}'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


