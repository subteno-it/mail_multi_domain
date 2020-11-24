# Copyright 2020 Subteno IT
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'

    force_alias_domain = fields.Char(
        string='Alias domain'
    )
