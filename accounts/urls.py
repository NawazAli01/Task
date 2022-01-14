from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
#from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    #path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
