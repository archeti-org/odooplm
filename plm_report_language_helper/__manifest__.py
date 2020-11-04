# -*- encoding: utf-8 -*-
##############################################################################
#
#    OmniaSolutions, Open Source Management Solution    
#    Copyright (C) 2010-2011 OmniaSolutions (<http://www.omniasolutions.eu>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Plm Report Language Helper',
    'version': '14.0.1',
    'author': 'OmniaSolutions',
    'website': 'http://www.omniasolutions.eu',
    'category': 'Product Lifecycle Management',
    'sequence': 15,
    'summary': '',
    'license': 'AGPL-3',
    'images': [],
    'depends': ['plm', 'plm_spare'],
    'description': """Manage multilanguage PLM reports
    """,
    'data': [# security
             'security/plm_security.xml',
             # views
             'views/plm_component_action_extended.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
