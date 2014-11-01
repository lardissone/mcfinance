from django.conf.urls import patterns, url

urlpatterns = patterns('',

    # Core
    url(r'^$',
        'mcfinance.core.views.dashboard',
        name='dashboard'),
    url(r'^switch-account/(?P<account_id>[0-9a-f]{24})/$',
        'mcfinance.core.views.switch_account',
        name='switch-account'),


)
