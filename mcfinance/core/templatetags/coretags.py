from django import template

from mcfinance.transactions.documents import Account, Category, Payee


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


def sidebar(context):
    accounts = Account.objects.order_by('name')
    categories = Category.objects.order_by('name')
    payees = Payee.objects.order_by('name')

    return {
        'accounts': accounts,
        'categories': categories,
        'payees': payees,
    }

register.inclusion_tag(
    'core/_sidebar.html',
    takes_context=True)(sidebar)
