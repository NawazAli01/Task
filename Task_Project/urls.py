"""Task_Project URL Configuration

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
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.urlpatterns import format_suffix_patterns
from task_app import views
from django.contrib.auth import views
from django.views.generic.base import TemplateView
#from api.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
# router.register(r'product', ProductViewSet, basename='Product')
# router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name ='token_obtain_pair'),
    path('api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name ='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
