from django.utils.translation import ugettext as _
from django import forms
from mcfinance.transactions.documents import Account, ACCOUNT_TYPES

CURRENCIES = (
    ('ARS', _('ARS - Argentine Peso')),
    ('USD', _('USD - United States Dollar')),
)


class AccountForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Name')})
    )
    account_type = forms.ChoiceField(
        initial='savings',
        choices=tuple(ACCOUNT_TYPES.items())
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': _('Description')}),
        required=False
    )
    currency = forms.ChoiceField(
        initial="ARS",
        choices=CURRENCIES
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        self.id = instance.id if instance else None
        return super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name'].strip(' ')
        if self.id and Account.objects(name=name).count():
            raise forms.ValidationError(_('This name is already in use.'))

        return name
