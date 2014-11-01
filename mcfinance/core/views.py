from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.contrib import messages

import pygal
from pygal.style import DarkSolarizedStyle

from mcfinance.transactions.documents import Transaction, Account


def dashboard(request):

    total = 0
    cats = {}

    selected_account = request.session.get('selected_account')
    if selected_account:
        account = Account.objects(id=selected_account).first()
    else:
        # TODO: if not account selected, global stats
        account = Account.objects().first()

    filters = {}
    if Account.objects().count() > 0:
        filters = {'account': account}

    for t in Transaction.objects(**filters):
        total += t.amount * (-1 if t.transaction_type == 'expense' else 1)
        if t.category.name not in cats:
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


def switch_account(request, account_id):

    account = Account.objects(id=account_id).first()

    if not account:
        messages.error(request, _('Account doesn\'t exists.'))
        return redirect('dashboard')

    request.session['selected_account'] = str(account.id)
    messages.success(request, _('Account changed to %s.') % account.name)

    return redirect('dashboard')
