from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from xploitSOP_CORS_CSRF import views

urlpatterns = [
    path('', views.index),
    path('run', views.run),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
