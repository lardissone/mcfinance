from django.apps import AppConfig, apps


class TransactionsConfig(AppConfig):

    label = 'mcfinance_transactions'
    verbose_name = 'MC Finance Transactions'
    name = 'mcfinance.transactions'
    models_module = 'mcfinance.transactions.documents'
