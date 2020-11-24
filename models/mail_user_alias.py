# Copyright 2020 Subteno IT
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class MailUserAlias(models.Model):
    _name = 'mail.user.alias'
    _order = 'id'

    name = fields.Char(
        string='Name',
        required=True,
    )
    email = fields.Char(
        string='Email',
        required=True,
    )
    alias_domain = fields.Char(
        string='Alias Domain',
        required=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=True,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.user.company_id.id
    )

    _sql_constraints = [
        ('email_uniq', 'unique(email,alias_domain)', 'Email should be unique!')
    ]
