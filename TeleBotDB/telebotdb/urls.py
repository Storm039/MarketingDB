"""telebotdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from users.views import *
from marketing.views import *
from company.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/users/", UsersApiList.as_view()),
    path("api/v1/validusers/", ValidUsersApiList.as_view()),
    path("api/v1/userupdate/<int:pk>/", UsersApiUpdate.as_view()),
    path("api/v1/userdelete/<int:pk>/", UsersApiDestroy.as_view()),
    path("api/v1/usercreate/", UsersApiCreate.as_view()),
    path("api/v1/promotions/", PromotionsApiList.as_view()),
    path("api/v1/promotioncreate/", PromotionsApiCreate.as_view()),
    path("api/v1/company/<int:pk>/", CompanyApiInfo.as_view()),
    path("api/v1/companyconfig/", ConfigDataApiInfo.as_view()),
    path("api/v1/bonusesinfo/", BonusesApiInfo.as_view()),
    path("api/v1/bonusesupdate/", BonusesApiUpdate.as_view()),
]
