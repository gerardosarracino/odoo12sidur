# -*- coding: utf-8 -*-

from odoo import models, fields


class Datos(models.Model):
    _name = 'contratista.datos'

    name = fields.Char(string="Nombre/Razón social:")
    persona_moral = fields.Boolean(string="Persona Moral:", required=True)
    persona_fisica = fields.Boolean(string="Persona Física:", required=True)
    activo = fields.Boolean(string="Activo:", required=True)
    rfc = fields.Char(string="RFC:", required=True)
    select = [('mexicana', 'MEXICANA'), ('extranjera', 'EXTRANJERA')]
    nacionalidad = fields.Selection(select, string="Nacionalidad:", required=True)
    acreditacion_empresa = fields.Text(string="Acreditación Empresa:", required=True)
    calles = fields.Char(string="Calles:", required=True)
    numero = fields.Char(string="Número:", required=True)
    colonia = fields.Char(string="Colonia:", required=True)
    cp = fields.Char(string="C.P.:", required=True)
    municipio_delegacion = fields.Char(string="Municipio/Delegación:", required=True)
    estados = [('AGC', "Aguascalientes"), ('BCN', "Baja California Norte"), ('BCS', "Baja California Sur"),
               ('CAMP', "Campeche"), ('CHI', "Chiapas"), ('CHIH', "Chihuahua"), ('COA', "Coahuila"), ('COL', "Colima"),
               ('DF', "Distrito Federal"), ('DUR', "Durango"), ('EM', "Estado de Mexico"), ('GTO', "Guanajuato"),
               ('GRO', "Guerrero"), ('HDO', "Hidalgo"), ('JCO', "Jalisco"), ('MCH', "Michoacan"), ('MRO', "Morelos"),
               ('NR', "Nayarit"), ('NLN', "Nuevo Leon"), ('OXC', "Oaxaca"), ('PUE', "Puebla"), ('QRT', "Queretaro"),
               ('QTR', "Quintana Roo"), ('SNL', "San Luis Potosi"), ('SIN', "Sinaloa"), ('SONORA', "Sonora"),
               ('TBC', "Tabasco"), ('TMP', "Tamaulipas"), ('TXL', "Tlaxcala"), ('VER', "Veracruz"), ('YCT', "Yucatan"),
               ('ZAC', "Zacatecas")]
    estado_entidad = fields.Selection(estados, string="Estado/Entidad", required=True)
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