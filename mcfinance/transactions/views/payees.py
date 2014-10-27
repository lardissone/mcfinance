from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.contrib import messages

from mcfinance.transactions.documents import Payee
from mcfinance.transactions.forms.payees import PayeeForm


def payee_list(request):
    return render(request, 'payees/list.html', {
        'results': Payee.objects.all(),
        'section_title': _('Payees')
    })

def payee_form(request, payee_id=None):
    payee = Payee.objects(id=payee_id).first() if payee_id else Payee()

    if request.POST:
        form = PayeeForm(request.POST)

        if form.is_valid():
            payee.populate(form.cleaned_data)
            payee.save()
            messages.success(request, _('Payee successfully saved.'))
            return redirect('payee-edit', payee_id=payee.id)

    else:
        form = PayeeForm(initial={
            'name': payee.name,
            'address': payee.address,
            'description': payee.description,
        })

    return render(request, 'payees/form.html', {
        'form': form,
        'section_title': _('Edit payee') if payee_id else _('Create payee')
    })


def payee_delete(request, payee_id=None):
    payee = Payee.objects(id=payee_id).first()
    if payee:
        payee.delete()
        messages.success(request, _('Payee successfully removed.'))

    return redirect('payee-list')
