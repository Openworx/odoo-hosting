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

from openerp.http import request
from openerp.osv import orm, osv, fields


class View(osv.osv):
    _inherit = "ir.ui.view"

    def render(self, cr, uid, id_or_xml_id, values=None, engine='ir.qweb', context=None):

        if not values:
            values = {}

        website = self.pool.get('ir.model.data').get_object(cr, uid, 'website', 'default_website')
        values['piwik_url'] = website.piwik_url
        values['piwik_site_id'] = website.piwik_site_id
        values['piwik_track_backend'] = website.piwik_track_backend

        return super(View, self).render(cr, uid, id_or_xml_id, values=values, engine=engine, context=context)
