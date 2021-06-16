# -*- coding: utf-8 -*-
# Copyright 2020 Subteno IT
# See LICENSE file for full copyright and licensing details.

from odoo import models, api


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def get_param(self, key, default=False):
        alias_domain = False
        if key == 'mail.catchall.domain':
            user_config = self.env['ir.config_parameter'].sudo().get_param('mail.split_server_mail_by_user')
            if user_config == 'False':
                if self.env.context.get('active_model') and \
                        self.env.context.get('active_id') and \
                        'force_alias_domain' in self.env[self.env.context['active_model']]._fields.keys():
                    alias_domain = self.env[self.env.context['active_model']].sudo(
                    ).browse(self.env.context['active_id']).force_alias_domain
                if not alias_domain and self._context.get('uid'):
                    alias_domain = self.env['res.users'].browse(self._context.get('uid')).company_id.sudo(
                    ).force_alias_domain
        return alias_domain or super(IrConfigParameter, self).get_param(key=key, default=default)
