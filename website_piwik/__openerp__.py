# -*- coding: utf-8 -*-
##############################################################################
#
# Author: Yannick Buron. Copyright Yannick Buron
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Piwik Analytics',
    'version': '1.0',
    'category': 'Tools',
    'complexity': "easy",
    'description': """
Piwik Analytics.
=================

Collects web application usage with Piwik.
    """,
    'author': 'OpenERP SA',
    'website': 'https://github.com/YannickB/odoo-hosting',
    'depends': ['website'],
    'data': [
        'views/res_config.xml',
        'views/website_templates.xml',
        'views/website_views.xml',
    ],
    'installable': True,
    'active': False,
}

