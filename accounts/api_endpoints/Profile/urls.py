from django.urls import path
from accounts.api_endpoints.Profile import *
from accounts.api_endpoints.Register.views import RegisterUserAPIView, RegisterConfirmAPIView
from accounts.api_endpoints.SaveProduct import SavedProductsListAPIView, SaveProductAPIView


app_name = 'profile'

urlpatterns = [
    path('profile/delete/', ProfileDeleteAPIView.as_view(), name="profile"),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name="profile-update"),

    path('password-reset/request/', PasswordResetRequestAPIView.as_view(), name="password-reset"),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
    
    path('register/', RegisterUserAPIView.as_view(), name="register"),
    path('register/confirm/', RegisterConfirmAPIView.as_view(), name="register-confirm"),

    path('saved-products/', SavedProductsListAPIView.as_view(), name="saved-products"),
    path('save-product/', SaveProductAPIView.as_view(), name="save-product"),
]
