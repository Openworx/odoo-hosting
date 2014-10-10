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

from openerp.osv import fields, osv


class WebsiteConfigSettings(osv.osv_memory):
    _inherit = 'website.config.settings'

    _columns = {
        'piwik_url': fields.related('website_id', 'piwik_url', type="char", string='Piwik Analytics URL'),
        'piwik_site_id': fields.related(
            'website_id', 'piwik_site_id',
            type="integer", string='Piwik Analytics SiteId'
        ),
        'piwik_track_backend': fields.related(
            'website_id', 'piwik_track_backend',
            type="boolean", string='Piwik Track Backend'
        ),
    }
