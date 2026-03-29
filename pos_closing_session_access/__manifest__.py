{
    'name': "POS Session Close Access Control",

    'summary': "Restrict POS session closing to authorized users only",

    'description': """
POS Session Close Access Control
================================

This module allows administrators to control which users are allowed 
to close Point of Sale (POS) sessions.

Key Features
------------
* Adds a checkbox **'Access for Closing POS'** in the Users form.
* Only users with this permission enabled can close a POS session.
* Unauthorized users will receive a warning popup when attempting to close the register.
* Helps improve operational security in retail environments.

How It Works
------------
1. A new field **'Access for Closing POS'** is added to the Users form.
2. When a user tries to close a POS session, the system checks the user's permission.
3. If the permission is not enabled, the system prevents the session from closing and displays an alert.

Benefits
--------
* Prevents accidental or unauthorized POS session closure.
* Adds better control over cashier operations.
* Improves store workflow management.

Compatible with Odoo POS interface.
    """,

    'author': "Apurva Wanjari",
    'website': "https://apps.odoo.com/apps/modules/browse?search=apurva+wanjari",

    'category': 'Point of Sale',
    'version': '18.0.1.0.0',

    'depends': [
        'base',
        'point_of_sale',
    ],

    'data': [
        'views/res_users_view.xml',
    ],

    'assets': {
        'point_of_sale._assets_pos': [
            'pos_closing_session_access/static/src/js/close_session_restriction.js',
        ],
    },

    "images": ["static/description/banner.png"],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
