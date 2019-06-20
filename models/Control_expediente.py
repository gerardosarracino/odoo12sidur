# -*- coding: utf-8 -*-

from odoo import models, fields


class ExpedienteUnico(models.Model):
    _name = 'control_expediente.control_expediente'

    select_etapa = [('1', 'PREVIO AL PROCESO DE CONTRATACIÓN'), ('2', 'DURANTE EL PROCESO DE CONTRATACIÓN'),
                    ('3', 'DESPUÉS DEL PROCEDIMIENTO DE CONTRATACIÓN Y ANTES DE EJECUTAR LA OBRA'),
                    ('4', 'DURANTE LA EJECUCIÓN DE LA OBRA'), ('5', 'DESPUÉS DE LA EJECUCIÓN DE LA OBRA')]
    etapa = fields.Selection(select_etapa, string="Etapa:", required=True)
    responsable = fields.Many2one(
        comodel_name='res.users',
        string='Responsable:',
        default=lambda self: self.env.user.id,
        required=True
    )
    nombre = fields.Char(string="Nombre:", required=True)
    orden = fields.Char(string="Orden:", required=True)
