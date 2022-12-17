from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from xploitSOP_CORS_CSRF import views


urlpatterns = [
    path('', views.index),
    path('run', views.run),
    path('chg_pwd_get', views.chg_pwd_get),
    path('chg_pwd_post', views.chg_pwd_post),
    path('chg_pwd_json', views.chg_pwd_json),
    path('chg_pwd_std', views.chg_pwd_std),
    path('chg_pwd_permissive', views.chg_pwd_permissive_cors),
    path('chg_pwd_wildcard', views.chg_pwd_wildcard),
    path('chg_pwd_null_origin', views.chg_pwd_null_origin),
    path('my_balance_cors', views.my_balance_permissive_cors),
    path('my_balance_no_cors', views.my_balance_no_cors)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
