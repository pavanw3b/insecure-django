from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from xploitpp import views


urlpatterns = [
    path('', views.index),
    path('welcome', views.welcome),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
