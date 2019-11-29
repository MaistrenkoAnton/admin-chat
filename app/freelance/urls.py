"""freelance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.contrib.auth import views as auth_views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from material.admin.sites import site
from rest_framework import permissions

from users.views import PasswordResetConfirmView

site.site_header = _('Administration')
site.site_title = _('Marketplace')
site.main_hover_color = '#969999'
site.main_bg_color = '#41adda'

site.favicon = staticfiles('admin/favicon.ico')
site.profile_picture = staticfiles('admin/logo.jpg')
site.profile_bg = staticfiles('admin/profile_bg.png')
site.login_logo = staticfiles('admin/logo.jpg')
site.logout_bg = staticfiles('admin/logout_bg.png')

schema_view = get_schema_view(
   openapi.Info(
      title="Freelance API",
      default_version='v1',
      description="Freelance API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('chat/', include('chat.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + i18n_patterns(
    path('admin/', include('material.admin.urls'), name='admin'),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('admin/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('', RedirectView.as_view(url='admin/', permanent=False), name='home'),
    prefix_default_language=False
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
