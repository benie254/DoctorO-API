"""
URL configuration for doc_proj project.

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
from django.urls import path, include, re_path as url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from doc_app import views 
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="DrOwiti API",
      default_version='v1',
      description="Back-end logic for a psychiatrist's landing page",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="fullstack.benie@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('',views.Landing,name="landing"),
    url(r'^openapi/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/',include('doc_app.urls')),
]
