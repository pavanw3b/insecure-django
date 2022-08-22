from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from xploitSSRF import views

urlpatterns = [
    path('', views.index),
    path('import', views.import_linkedin_url),
    path('api/admin/reset', views.api_admin_password_reset),
    path('api', views.api_documentation)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
