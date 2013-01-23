from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead,current_datetime2, current_datetime3, current_datetime4,display_meta
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    ('^hello/$',hello),
    ('^now/$',current_datetime),
    ('^now2/$',current_datetime2),
    ('^now3/$',current_datetime3),
    ('^now4/$',current_datetime4),
    ('^time/plus/(\d{1,2})/$',hours_ahead),
    ('^meta/$',display_meta),
)
