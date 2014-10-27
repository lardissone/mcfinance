from django.conf.urls import patterns, url

urlpatterns = patterns('',

    # Core
    url(r'^$',
        'mcfinance.core.views.dashboard',
        name='dashboard'),
)
