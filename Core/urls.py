"""
URL configuration for Core project.

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
from apps.main.views.docs import docs_login_view
from rest_framework.permissions import IsAdminUser
from rest_framework.documentation import include_docs_urls
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('apps.cars.urls')),
    path('users/', include('apps.users.urls')),
    path('fiter/', include('apps.filter.urls')),
    path('services/', include('apps.services.urls')),
    path('specifications/', include('apps.specifications.urls')),
    path('token/access/admin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('docs/login/', docs_login_view),
    path(r'docs/', 
        include_docs_urls(
            title='OrientMotors',
            authentication_classes=[SessionAuthentication],
            permission_classes=[IsAdminUser]
        ), 
    ),
]
