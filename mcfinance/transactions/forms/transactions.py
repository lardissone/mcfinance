from django.utils.translation import ugettext as _
from django import forms
from mcfinance.transactions.documents import (
        Transaction,
        Account,
        Payee,
        Category,
        TRANSACTION_TYPES)
import datetime


class TransactionForm(forms.Form):
    account = forms.ChoiceField(
        choices=[(str(a.id), a.name) for a in Account.objects.all()],
        required=True
    )
    transaction_type = forms.ChoiceField(
        choices=tuple(TRANSACTION_TYPES.items()),
        required=True,
        widget=forms.RadioSelect(),
        initial='expense'
    )
    payee = forms.ChoiceField(
        choices=[(str(p.id), p.name) for p in Payee.objects.all()],
        required=True
    )
    category = forms.ChoiceField(
        choices=[(str(c.id), c.name) for c in Category.objects.all()],
        required=True
    )
    date = forms.DateField(
        initial=datetime.date.today
    )
    amount = forms.DecimalField(required=True)
    description = forms.CharField(
        widget=forms.Textarea(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        self.id = instance.id if instance else None
        return super().__init__(*args, **kwargs)
