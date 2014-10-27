from django.utils.translation import ugettext as _
from django import forms
from mcfinance.transactions.documents import Category


class CategoryForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Name')})
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
        if self.id and Category.objects(name=name).count():
            raise forms.ValidationError(_('This category is already in use.'))

        return name
