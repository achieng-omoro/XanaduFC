"""FOOTBALLCLUB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.templatetags.static import static
from django.views.generic.base import RedirectView
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
from rest_framework import routers
from Xanadufc.views import BlogView


router=routers.DefaultRouter()
router.register('',BlogView)


urlpatterns = [
    path('xanadu/', admin.site.urls),
    path('',include('Xanadufc.urls',namespace='Xanadu')),
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'))),
    path('api',include(router.urls))
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'Xanadufc.views.error_404'