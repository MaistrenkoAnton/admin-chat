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

from material.admin.sites import site

site.site_header = _('Administration ')
site.site_title = _('Marketplace')
site.main_hover_color = '#969999'
site.main_bg_color = '#41adda'

site.favicon = staticfiles('admin/favicon.ico')
site.profile_picture = staticfiles('admin/logo.jpg')
site.profile_bg = staticfiles('admin/profile_bg.png')
site.login_logo = staticfiles('admin/logo.jpg')
site.logout_bg = staticfiles('admin/logout_bg.png')


urlpatterns = i18n_patterns(
    path('admin/', include('material.admin.urls'))
) + [
    path('', RedirectView.as_view(url='en/admin/', permanent=False), name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
