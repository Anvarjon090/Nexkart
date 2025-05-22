from django.urls import path

from common.views import HomeView, ContactView

app_name = "common"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
]