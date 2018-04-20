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
    url(r'^upsertivhun/(?P<ivhun_id>[0-9]+)/$', 'signups.views.upsertivhun', name='upsertivhun'),
    url(r'^copyivhun/(?P<ivhun_id>[0-9]+)/$', 'signups.views.copyivhun', name='copyivhun'),
    url(r'^confirmdelete/(?P<ivhun_id>[0-9]+)/$', 'signups.views.confirmdelete', name='confirmdelete'),
    url(r'^deleteivhun/(?P<ivhun_id>[0-9]+)/$', 'signups.views.deleteivhun', name='deleteivhun'),
    url(r'^emailivhun/(?P<ivhun_id>[0-9]+)/$', 'signups.views.emailivhun', name='emailivhun'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)