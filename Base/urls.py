"""BuildMelter URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include as incl
import os

admin.site.site_header = 'Melter Adminitstration'
admin.site.site_title = 'Melter'
# admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'Melter Admin'
admin.empty_value_display = '**Empty**'


APPS_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# TODO: UNCOMMENTS APPS AS THEY BECOME FUNCTIONAL
urlpatterns = [
    path('admin/', admin.site.urls),



    url('', incl('Apps.BuildManager.urls')),
    # url('builds', incl('Apps.BuildManager.urls')),
    # url('builds/', incl('Apps.BuildManager.urls')),
    # url('build', incl('Apps.BuildManager.urls')),
    # url('build/', incl('Apps.BuildManager.urls')),

    url('', incl('Apps.ReachOut.urls')),


    url('', incl('Apps.Sprints.urls')),


    url('', incl('Apps.TaskPage.urls')),


    url('', incl('Apps.TestViews.urls')),

    #path('basicstatus/', include('basicstatus.urls')),
    # Redirect base page to basicstatus page
    #url(r'^$', incl('basicstatus.urls')),
    #path('overviews/', include('overviews.urls')),
    #path('sprints/', include('sprints.urls')),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
