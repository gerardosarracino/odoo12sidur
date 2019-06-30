# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Documento(models.Model):
    _name = 'plantillas.documento'

    @api.multi
    def _compute_tipo_documento_text(self):
        for order in self:
            documento_names = [documento.name_id.name for documento in Documento.documento]
            Documento.name = "\n".join(documento_names)

    name = fields.Text(string="Tipo de documento",
                              compute='_compute_tipo_documento_text',
                              store=True)

    documento = fields.One2many("plantillas.plantillas", "tipo_documento")


class Plantilla(models.Model):
    _name = 'plantillas.plantillas'

    select_normatividad = [('1', 'FEDERAL'), ('2', 'ESTATAL/LOCAL'), ('3', 'TODOS')]
    select_periodo = [('1', 'ANUAL'), ('2', 'MULTIANUAL'), ('3', 'TODOS')]
    select_anticipo = [('1', 'SI'), ('2', 'NO'), ('3', 'TODOS')]
    select_tipo_procedimiento = [('1', 'ADJUDICACIÓN DIRECTA'), ('2', 'ADJUDICACIÓN POR EXCEPCIÓN O EMERGENCIA'),
                                 ('3', 'INVITACIÓN RESTRINGIDA'), ('4', 'LICITACION NACIONAL'), ('5', 'TODOS')]
    # -----
    tipo_documento = fields.Many2one('plantillas.documento', string="Tipo de documento",
                                     required=True)

    normatividad = fields.Selection(select_normatividad, string="Normatividad:", required=True)
    programa = fields.Many2one(comodel_name="generales.programas_inversion", inverse_name="name", string="Programa:")
    periodo = fields.Selection(select_periodo, string="Periodo:", required=True)
    anticipo = fields.Selection(select_anticipo, string="Anticipo:", required=True)
    tipo_procedimiento = fields.Selection(select_tipo_procedimiento, string="Tipo de Procedimiento:", required=True)
    subir_documento = fields.Binary(string="Subir Documento:")
    nombre_documento = fields.Char(string="Nombre del Documento:")

