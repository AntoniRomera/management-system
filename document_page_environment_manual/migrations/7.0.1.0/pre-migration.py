# -*- encoding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from openupgrade import openupgrade
from openupgrade.openupgrade import logged_query


def pre_migrate_environment_manual_category(cr, version):
    logged_query(cr, """\
UPDATE document_page
SET parent_id = (SELECT id FROM document_page WHERE name = 'Manuals' LIMIT 1),
    name = name || ' (' || %s || ')'
WHERE name = 'Environment Manual' AND type = 'content';""", [version])
    logged_query(cr, """\
UPDATE document_page
SET name = name || ' (' || %s || ')'
WHERE name = 'Environment Manual' AND type = 'category';""", [version])


@openupgrade.migrate()
def migrate(cr, version):
    pre_migrate_environment_manual_category(cr, version)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: