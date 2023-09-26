from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from apps.kolobanga.views import send_bot_info


urlpatterns = [
    path('', TemplateView.as_view(template_name="kolobanga/home.html")),
    path('send_info/', send_bot_info, name="send_bot_info")
]
