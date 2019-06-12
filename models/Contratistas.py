# -*- coding: utf-8 -*-

from odoo import models, fields


class TipoContratista(models.Model):
    _name = 'contratista.tipo_contratista'

    persona_moral = fields.Boolean(string="Persona Moral:", required=True)
    persona_fisica = fields.Boolean(string="Persona Física:", required=True)
    activo = fields.Boolean(string="Activo:", required=True)


class Datos(models.Model):
    _name = 'contratista.datos'

    name = fields.Char(string="Nombre/Razón social:")
    rfc = fields.Char(string="RFC:", required=True)
    select = [('mexicana', 'MEXICANA'), ('extranjera', 'EXTRANJERA')]
    nacionalidad = fields.Selection(select, string="Nacionalidad:", required=True)
    acreditacion_empresa = fields.Text(string="Acreditación Empresa:", required=True)
    calles = fields.Char(string="Calles:", required=True)
    numero = fields.Char(string="Número:", required=True)
    colonia = fields.Char(string="Colonia:", required=True)
    cp = fields.Char(string="C.P.:", required=True)
    municipio_delegacion = fields.Char(string="Municipio/Delegación:", required=True)
    # relacion hecha hacia generales.municipios, pero sin vista no se puede verificar funcionamiento, pendiente
    # estado_entidad = fields.Many2one(comodel_name="generales.municipios", string="Estado/Entidad:",
    #                                  required=True)
    estado_entidad = fields.Char(string="Estado/Entidad:", required=True)
    telefono = fields.Char(string="Teléfonos:", required=True)
    correo = fields.Char(string="Correo:", required=True)
    registro_concursante = fields.Char(string="Registro de Concursante:", required=True)
    objeto_social = fields.Text(string="Objeto Social:", required=True)


class RepresentanteLegal(models.Model):
    _name = 'contratista.representante_legal'

    name = fields.Char(string="Nombre del Representante:", required=True)
    caracter = fields.Char(string="Carácter:", required=True)
    acreditacion = fields.Text(string="Acreditación:", required=True)
    documento_acredita_nacionalidad = fields.Char(string="Documento con el que acredita su Nacionalidad:", required=True)
    rfc = fields.Char(string="RFC:", required=True)
    numero_indentificacion = fields.Char(string="Número de Identificación:", required=True)
    expedida_por = fields.Char(string="Expedida por:", required=True)