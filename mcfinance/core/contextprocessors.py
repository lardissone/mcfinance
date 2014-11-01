from mcfinance.transactions.documents import Account


def mcvars(request):
    output = {}

    selected_account = request.session.get('selected_account')
    if selected_account:
        selected_account = Account.objects(id=selected_account).first()
    output['selected_account'] = selected_account

    return output
