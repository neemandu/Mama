from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thank-you', 'signups.views.thankyou', name='thankyou'),
    url(r'^home', 'signups.views.home', name='home'),
    url(r'^allivhunim', 'signups.views.allivhunim', name='allivhunim'),
    url(r'^newpatient/(?P<ivhun_id>[0-9]+)/$', 'signups.views.newpatient', name='newpatient'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)