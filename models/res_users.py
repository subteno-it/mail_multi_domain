# -*- coding: utf-8 -*-
# Copyright 2020 Subteno IT
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    mail_user_alias_ids = fields.One2many(
        comodel_name='mail.user.alias',
        inverse_name='user_id',
    )
