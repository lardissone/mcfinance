from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', include('mcfinance.core.urls')),

    url(r'', include('mcfinance.transactions.urls')),
)
