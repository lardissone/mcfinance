from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.contrib import messages

from mcfinance.transactions.documents import Account
from mcfinance.transactions.forms.accounts import AccountForm


def account_list(request):
    return render(request, 'accounts/list.html', {
        'results': Account.objects.all(),
        'section_title': _('Accounts')
    })

def account_form(request, account_id=None):
    account = Account.objects(id=account_id).first() if account_id else Account()

    if request.POST:
        form = AccountForm(request.POST)

        if form.is_valid():
            account.populate(form.cleaned_data)
            account.save()
            messages.success(request, _('Account successfully saved.'))
            return redirect('account-edit', account_id=account.id)

    else:
        form = AccountForm(initial={
            'name': account.name,
            'description': account.description,
            'account_type': account.account_type,
            'currency': account.currency,
        })

    return render(request, 'accounts/form.html', {
        'form': form,
        'section_title': _('Edit account') if account_id else _('Create account')
    })


def account_delete(request, account_id=None):
    account = Account.objects(id=account_id).first()
    if account:
        account.delete()
        messages.success(request, _('Account successfully removed.'))

    return redirect('account-list')
