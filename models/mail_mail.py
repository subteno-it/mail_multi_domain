# Copyright 2020 Subteno IT
# See LICENSE file for full copyright and licensing details.

from odoo import models, api
from odoo.tools import formataddr


class MailMail(models.Model):
    _inherit = 'mail.mail'

    def _split_by_server(self):
        user_config = self.env['ir.config_parameter'].sudo().get_param('mail.split_server_mail_by_user')
        for mail in self.filtered(lambda r: not r.mail_server_id):
            user = self.env['res.users'].search([('partner_id', '=', mail.author_id.id)])

            if user_config == 'True':
                server_id = user.server_mail_id
                if not server_id:
                    alias_domain = user.company_id.sudo().force_alias_domain
                    server_id = self.env['ir.mail_server'].search([('force_alias_domain', '=', alias_domain)])

                partner = user.partner_id
                mail.mail_server_id = server_id
                mail.email_from = formataddr((
                    partner.name,
                    partner.email
                ))
            else:
                alias_domain = ''
                if 'force_alias_domain' in self.env[mail.model]._fields.keys():
                    alias_domain = self.env[mail.model].sudo().browse(mail.res_id).force_alias_domain
                if not alias_domain:
                    alias_domain = user.company_id.sudo().force_alias_domain
                if alias_domain:
                    company_server_id = self.env['ir.mail_server'].search(
                        [('force_alias_domain', '=', alias_domain)])
                    partner = user.mail_user_alias_ids.filtered(
                        lambda r: r.alias_domain == alias_domain) or user.partner_id
                    mail.mail_server_id = company_server_id
                    mail.email_from = formataddr((
                        partner.name,
                        partner.email.split('@')[0] + '@' + alias_domain
                    ))

        return super(MailMail, self)._split_by_server()
