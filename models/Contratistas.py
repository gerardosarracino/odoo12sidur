# -*- coding: utf-8 -*-

from odoo import models, fields


class TipoContratista(models.Model):
    _name = 'contratista.tipo_contratista'

    persona_moral = fields.Boolean(string="Persona Moral", required=True)
    persona_fisica = fields.Boolean(string="Persona Física", required=True)
    activo = fields.Boolean(string="Activo", required=True)


class Datos(models.Model):
    _name = 'contratista.datos'

    name = fields.Char(string="Nombre/Razon social:")
    rfc = fields.Char(string="RFC:", required=True)
    select = [('MEXICANA', 'MEXICANA'), ('EXTRANJERA', 'EXTRANJERA')]
    nacionalidad = fields.Selection(select, string="Nacionalidad:", required=True)
    acreditacion_empresa = fields.Text(string="Acreditación Empresa:", required=True)
    calles = fields.Char(string="Calles:", required=True)
    numero = fields.Char(string="Numero:", required=True)
    colonia = fields.Char(string="Colonia:", required=True)
    cp = fields.Char(string="C.P.:", required=True)
    #municipio_delegacion = fields.Char(string="Municipio/Delegación:", required=True)
    #estado_entidad = fields.Char(string="Estado/Entidad:", required=True)
    telefono = fields.Char(string="Teléfonos:", required=True)
    correo = fields.Char(string="E-Mail:", required=True)
    registro_concursante = fields.Char(string="Registro de concursante:", required=True)
    objeto_social = fields.Text(string="Objeto Social:", required=True)


class RepresentanteLegal(models.Model):
    _name = 'contratista.representante_legal'

    name = fields.Char(string="Nombre del Representante:", required=True)
    caracter = fields.Char(string="Carácter:", required=True)
    acreditacion = fields.Text(string="Acreditación:", required=True)
    documento_acredita_nacionalidad = fields.Char(string="Documento con el que acredita su Nacionalidad:", required=True)
    RFC = fields.Char(string="RFC:", required=True)
    indentificacion_num = fields.Char(string="Identificación Núm:", required=True)
    expedida_por = fields.Char(string="Expedida por:", required=True)