"""
URL configuration for asoud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        'api/v1/category/',
        include('apps.category.urls.general_urls'),
    ),
    path(
        'api/v1/info/',
        include('apps.information.urls.general_urls'),
    ),
    path(
        'api/v1/region/',
        include('apps.region.urls.general_urls'),
    ),
    path(
        'api/v1/owner/market/',
        include('apps.market.urls.owner_urls'),
    ),
    path(
        'api/v1/owner/product/',
        include('apps.product.urls.owner_urls'),
    ),
    path(
        'api/v1/user/chat/',
        include('apps.chat.urls.user_urls'),
    ),
    path(
        'api/v1/user/comment/',
        include('apps.comment.urls'),
    ),
    path(
        'api/v1/user/market/',
        include('apps.market.urls.user_urls'),
    ),
    path(
        'api/v1/user/',
        include('apps.users.urls.user_urls'),
    ),
    path(
        'api/v1/discount/',
        include('apps.discount.urls'),
    )
]

admin.site.site_header = _('Asoud Administration')
admin.site.index_title = _('Welcome to Asoud Admin')
admin.site.site_title = _('Asoud Admin')
