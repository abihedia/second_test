from odoo import models, fields, api


class   AccountMoveLineHerit(models.Model):
    _inherit = "account.move.line"
    no = fields.Char("Numéro",default='0', store=True)


class AcountMoveHerit(models.Model):
    _inherit = 'account.move'
    somme      = fields.Monetary(compute="_somme_article_moves",default=0.0)
    @api.depends('invoice_line_ids')
    def _somme_article_moves(self):
        somme = 0
        for r in self:
            note = 0
            section = 0
            compt = 0
            for line in r.invoice_line_ids:
                if line.display_type == 'line_note' or line.display_type == 'line_section':
                    compt = 0
                if line.display_type == 'line_note':
                    note = note + 1
                    section = 0
                if line.display_type == 'line_section':
                    section = section + 1
                somme += line.quantity
                line.no = str(note) + str('.') + str(section) + str('.') + str(compt)
                compt = compt + 1
            r.somme = somme

