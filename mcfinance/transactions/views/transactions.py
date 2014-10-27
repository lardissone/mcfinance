from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.contrib import messages

import datetime

from mcfinance.transactions.documents import Transaction
from mcfinance.transactions.forms.transactions import TransactionForm


def transaction_list(request):
    return render(request, 'transactions/list.html', {
        'results': Transaction.objects.all(),
        'section_title': _('Transactions')
    })

def transaction_form(request, transaction_id=None):
    transaction = Transaction.objects(id=transaction_id).first() if transaction_id else Transaction()

    if request.POST:
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction.populate(form.cleaned_data)
            transaction.save()
            messages.success(request, _('Transaction successfully saved.'))
            return redirect('transaction-list')

    else:
        form = TransactionForm(initial={
            'account': str(transaction.account.id) if transaction.account else None,
            'transaction_type': transaction.transaction_type if transaction.transaction_type else 'expense',
            'payee': str(transaction.payee.id) if transaction.payee else None,
            'category': str(transaction.category.id) if transaction.category else None,
            'date': transaction.date.strftime('%Y-%m-%d') if transaction.date else datetime.date.today,
            'amount': transaction.amount,
            'description': transaction.description
        })

    return render(request, 'transactions/form.html', {
        'form': form,
        'section_title': _('Edit transaction') if transaction_id else _('Create transaction')
    })


def transaction_delete(request, transaction_id=None):
    transaction = Transaction.objects(id=transaction_id).first()
    if transaction:
        transaction.delete()
        messages.success(request, _('Transaction successfully removed.'))

    return redirect('transaction-list')
