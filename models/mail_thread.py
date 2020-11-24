# Copyright 2020 Subteno IT
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    force_alias_domain = fields.Char(
        string='Alias domain'
    )
