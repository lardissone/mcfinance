from django.utils.translation import ugettext as _
from django import forms
from mcfinance.transactions.documents import Payee


class PayeeForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Name')})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': _('Address')}),
        required=False
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': _('Description')}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        self.id = instance.id if instance else None
        return super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name'].strip(' ')
        if self.id and Payee.objects(name=name).count():
            raise forms.ValidationError(_('This payee is already in use.'))

        return name
