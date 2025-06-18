from django.urls import path

from accounts.api_endpoints import (
    SessionLoginAPIView,
    SessionLogoutAPIView,
    
)
from accounts.template_views import *

app_name = 'accounts'


apis = [
    path('session-login/', SessionLoginAPIView.as_view(), name="login-session"),
    path('session-logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    
]

template_urls = [
    path("template/register/", RegisterView.as_view(), name="register-template"),
    path("template/login/", LoginView.as_view(), name="login-template"),
    path("template/profile/", ProfileView.as_view(), name="profile-template"),
    # path("template/reset-password/", PasswordResetView.as_view(), name="reset-password-template"),
]

urlpatterns = apis + template_urls