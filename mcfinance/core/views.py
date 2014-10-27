from django.utils.translation import ugettext as _
from django.shortcuts import render


def dashboard(request):
    return render(request, 'core/dashboard.html', {
        'section_title': _('Dashboard'),
    })
