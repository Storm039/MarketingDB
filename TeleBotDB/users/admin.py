from django.contrib import admin
from .models import *
from marketing.models import *
from company.models import *


# Register your models here.
models = [Users,
          Company,
          Bonuses,
          Promotions,
          ConfigData,
          ]
admin.site.register(models)
