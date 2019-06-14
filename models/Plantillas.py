# -*- coding: utf-8 -*-

from odoo import models, fields


class Plantilla(models.Model):
    _name = 'platillas.plantilla'

    select_documento = [('1', 'INVITACIONES'), ('2', 'BASES'), ('3', 'VISITA A LA OBRA'), ('4', 'JUNTA ACLARACIONES'),
                        ('5', 'APERTURA DE PROPUESTAS'), ('6', 'FALLO'), ('7', 'CONTRATOS'), ('8', 'CONVENIOS'),
                        ('9', 'VERIFICACIÓN TERMINACIÓN'), ('10', 'RECEPCIÓN DE OBRA'), ('11', 'FINIQUITO'),
                        ('12', 'CIERRE ADMVO.'), ('13', 'EXT. DER. Y OBLIG'), ('14', 'TODOS')
                        ]
    select_normatividad = [('1', 'FEDERAL'), ('2', 'ESTATAL/LOCAL'), ('3', 'TODOS')]
    select_periodo = [('1', 'ANUAL'), ('2', 'MULTIANUAL'), ('3', 'TODOS')]
    select_anticipo = [('1', 'SI'), ('2', 'NO'), ('3', 'TODOS')]
    select_tipo_procedimiento = [('1', 'ADJUDICACIÓN DIRECTA'), ('2', 'ADJUDICACIÓN POR EXCEPCIÓN O EMERGENCIA'),
                                 ('3', 'INVITACIÓN RESTRINGIDA'), ('4', 'LICITACION NACIONAL'), ('5', 'TODOS')]
    # -----
    tipo_documento = fields.Selection(select_documento, string="Tipo de Documento:", required=True)
    normatividad = fields.Selection(select_normatividad, string="Normatividad:", required=True)
    # Relacion teoricamente hecha y funcional ---tener en cuenta al probar
    # programa = fields.Many2one(comodel_name="generales.programas_inversion", inverse_name="name", string="Programa:")
    programa = fields.Selection(string="Programa:", required=True)
    # - - - - -
    periodo = fields.Selection(select_periodo, string="Periodo:", required=True)
    anticipo = fields.Selection(select_anticipo, string="Anticipo:", required=True)
    tipo_procedimiento = fields.Selection(select_tipo_procedimiento, string="Tipo de Procedimiento:", required=True)

    # upload file en xml, <field name="subir_archivo" filename="nombre_archivo"/>
    #                     <field name="nombre_archivo" invisible="1"/>
    subir_archivo = fields.Binary(string="Subir Archivo:")
    nombre_archivo = fields.Char(string="Nombre del Archivo:")

    nombre_documento = fields.Char(string="Nombre de Documento:", required=True, )
