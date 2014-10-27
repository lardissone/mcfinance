from django.utils.translation import ugettext as _
from mongoengine import fields, Document, signals
from datetime import datetime


__all__ = (
    'Account',
    'Category',
    'Payee',
    'Transaction',
)

ACCOUNT_TYPES = {
    'savings': _('Savings'),
    'checking': _('Checking'),
    'cash': _('Cash'),
    'project': _('Project')
}
TRANSACTION_TYPES = {
    'expense': _('Expense'),
    'income': _('Income'),
}


class Account(Document):
    name = fields.StringField()
    description = fields.StringField()
    account_type = fields.StringField()
    currency = fields.StringField()

    def populate(self, data):
        self.name = data['name']
        self.description = data['description']
        self.account_type = data['account_type']
        self.currency = data['currency']


class Transaction(Document):
    account = fields.ReferenceField(Account)
    transaction_type = fields.StringField()
    date = fields.DateTimeField()
    category = fields.ReferenceField('Category')
    amount = fields.DecimalField()
    payee = fields.ReferenceField('Payee')
    description = fields.StringField()

    date_created = fields.DateTimeField(default=datetime.now())
    date_updated = fields.DateTimeField(default=datetime.now())

    def populate(self, data):
        self.account = Account.objects(id=data['account']).first()
        self.transaction_type = data['transaction_type']
        self.category = Category.objects(id=data['category']).first()
        self.payee = Payee.objects(id=data['payee']).first()
        self.date = data['date']
        self.amount = data['amount']
        self.description = data['description']

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        """Keep `date_updated` on sync"""
        document.date_updated = datetime.now()


class Payee(Document):
    name = fields.StringField()
    address = fields.StringField()
    description = fields.StringField()

    def populate(self, data):
        self.name = data['name']
        self.address = data['address']
        self.description = data['description']


class Category(Document):
    name = fields.StringField()
    description = fields.StringField()

    def populate(self, data):
        self.name = data['name']
        self.description = data['description']


signals.pre_save.connect(Transaction.pre_save, sender=Transaction)



