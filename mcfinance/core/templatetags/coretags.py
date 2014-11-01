from django import template

from mcfinance.transactions.documents import Account


register = template.Library()


@register.tag
def accounts_selector(context, selected_account):
    accounts = Account.objects.order_by('name')

    return {
        'accounts': accounts,
        'selected_account': selected_account
    }

register.inclusion_tag(
    'core/_accounts_selector.html',
    takes_context=True)(accounts_selector)


def getid(obj):
    return str(obj.id)
register.filter('getid', getid)
