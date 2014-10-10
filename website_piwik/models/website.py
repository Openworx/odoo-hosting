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

from openerp.osv import orm, osv, fields


class Website(osv.osv):

    _inherit = "website"

    _columns = {
        'piwik_url': fields.char('Piwik Analytics URL'),
        'piwik_site_id': fields.integer('Piwik Analytics SiteId'),
        'piwik_track_backend': fields.boolean('Piwik Track Backend?'),
    }
