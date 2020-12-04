from django.urls import path, include
from . import views as v

app_name = "accounts"

urlpatterns = [
    path('', v.Register_view, name="register"),
    ]