from django.utils.translation import ugettext as _
from django.shortcuts import render

import pygal
from pygal.style import DarkSolarizedStyle

from mcfinance.transactions.documents import Transaction


def dashboard(request):

    # TODO: filter by account

    total = 0
    cats = {}

    for t in Transaction.objects():
        total += t.amount * (-1 if t.transaction_type == 'expense' else 1)
        if not t.category.name in cats:
            cats[t.category.name] = 0
        cats[t.category.name] += t.amount

    cats_chart = pygal.Pie(
        style=DarkSolarizedStyle,
        width=300,
        height=300,
        legend_at_bottom=True,
        disable_xml_declaration=True)
    cats_chart.title = _('Categories')
    for c in cats.items():
        cats_chart.add(c[0], float(c[1]))

    return render(request, 'core/dashboard.html', {
        'section_title': _('Dashboard'),
        'total': total,
        'categories': cats,
        'cats_chart': cats_chart.render()
    })
