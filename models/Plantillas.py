# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Documento(models.Model):
    _name = 'plantillas.documento'
    # agrega el tipo de documento nomas
    name = fields.Char(string="Tipo de documento", required=True)
    # relacion con tipo_documento en la clase Plantilla, muestra los registros de documentos agregados.
    documento = fields.One2many("plantillas.plantillas", "tipo_documento")


class Plantilla(models.Model):
    _name = 'plantillas.plantillas'

    select_normatividad = [('1', 'FEDERAL'), ('2', 'ESTATAL/LOCAL'), ('3', 'TODOS')]
    select_periodo = [('1', 'ANUAL'), ('2', 'MULTIANUAL'), ('3', 'TODOS')]
    select_anticipo = [('1', 'SI'), ('2', 'NO'), ('3', 'TODOS')]
    select_tipo_procedimiento = [('1', 'ADJUDICACIÓN DIRECTA'), ('2', 'ADJUDICACIÓN POR EXCEPCIÓN O EMERGENCIA'),
                                 ('3', 'INVITACIÓN RESTRINGIDA'), ('4', 'LICITACION NACIONAL'), ('5', 'TODOS')]
    # -----
    # relacion hacia clase Documento, muestra los documentos agregados para elegir uno y almacenar todos los datos ahi.
    tipo_documento = fields.Many2one('plantillas.documento', string="Tipo de documento", required=True)

    normatividad = fields.Selection(select_normatividad, string="Normatividad:", required=True)
    programa = fields.Many2one(comodel_name="generales.programas_inversion", inverse_name="name", string="Programa:")
    periodo = fields.Selection(select_periodo, string="Periodo:", required=True)
    anticipo = fields.Selection(select_anticipo, string="Anticipo:", required=True)
    tipo_procedimiento = fields.Selection(select_tipo_procedimiento, string="Tipo de Procedimiento:", required=True)
    subir_documento = fields.Binary(string="Subir Documento:")
    nombre_documento = fields.Char(string="Nombre del Documento:")

