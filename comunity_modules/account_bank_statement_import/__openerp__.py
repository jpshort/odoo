# -*- encoding: utf-8 -*-
# noqa: This is a backport from Odoo. OCA has no control over style here.
# flake8: noqa
{
    'name': 'Account Bank Statement Import',
    'version': '1.0',
    'author': 'OpenERP SA',
    'depends': ['account'],
    'demo': [],
    'description' : """Generic Wizard to Import Bank Statements.
    
    Includes the import of files in .OFX format
    
    Backport from Odoo 9.0
    """,
    'data' : [
        'account_bank_statement_import_view.xml',
    ],
    'demo': [
        'demo/fiscalyear_period.xml',
        'demo/partner_bank.xml',
    ],
    'auto_install': False,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
