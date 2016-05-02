"""make_you URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from make_U import views as make_U_views
from django.views.generic import TemplateView
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

#url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),- 직접 템플릿에 연결

urlpatterns = [
    url(r'^pre_view/$',make_U_views.pre_view, name= 'pre_view'),
    url(r'^template/(?P<username>[0-9a-zA-Z]+)$',make_U_views.select_temp, name = 'select_temp'),
    url(r'^edit/(?P<username>[0-9a-zA-Z]+)$',make_U_views.edit, name = 'edit'),
    url(r'^result_join/(?P<username>[0-9a-zA-Z]+)$',make_U_views.result_join, name="result_join"),
    url(r'^join/$',make_U_views.join, name = 'join'),
    url(r'^$', make_U_views.main, name='main'),
    url(r'^login/$',login,{'template_name': 'login.html'},name = "login_url"),
    url(r'^logout/$',logout,{'next_page': '/login/'},name = "logout_url"),
    url(r'^admin/', admin.site.urls),

]

urlpatterns += static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
)
