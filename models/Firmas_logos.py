# -*- coding: utf-8 -*-

from odoo import models, fields


class FirmasLogos(models.Model):
    _name = 'firmas_logos.firmas_logos'
    # MUNICIPIO ?
    select = [('sidur', 'SIDUR')]
    municipio = fields.Selection(select, string="Municipio:", required=True)
    # DEPENDENCIA INSTITUCION
    name = fields.Char(string="Nombre:", required=True)
    image = fields.Binary("Image", help="This field holds the image used as avatar for ")
    # in xml, <field name="image" widget='image' class="oe_avatar"/>
    declaraciones_dependencia = fields.Text(string="Declaraciones Dependencia:", required=True)
    titular = fields.Char(string="Titular:", required=True)
    domicilio = fields.Text(string="Domicilio:", required=True)
    # TITULAR
    nombre_titular = fields.Char(string="Nombre:", required=True)
    puesto_titular = fields.Char(string="Puesto:", required=True)
    fecha_nombramiento_titular = fields.Date(string="Fecha de Nombramiento:", required=True)
    # CONTRALORIA INTERNA
    nombre_contraloria = fields.Char(string="Representante:", required=True)
    puesto_contraloria = fields.Char(string="Puesto:", required=True)
    fecha_nombramiento_contraloria = fields.Date(string="Fecha Nombramiento:", required=True)
    # REPRESENTANTE CIUDADANO
    nombre_representante_ciudadano = fields.Char(string="Nombre:", required=True)
    puesto_representante_ciudadano = fields.Char(string="Puesto:", required=True)
    # DIRECTOR / COORDINADOR ADMINISTRATIVO
    nombre_coordinador_administrativo = fields.Char(string="Nombre:", required=True)
    puesto_coordinador_administrativo = fields.Char(string="Puesto:", required=True)
    # DIRECTOR / COORDINADOR PLANEACION
    nombre_coordinador_planeacion = fields.Char(string="Nombre:", required=True)
    puesto_coordinador_planeacion = fields.Char(string="Puesto:", required=True)
    # DIRECTOR / COORDINADOR JURIDICO
    nombre_coordinador_juridico = fields.Char(string="Nombre:", required=True)
    puesto_coordinador_juridico = fields.Char(string="Puesto:", required=True)
    # RESPONSABLE / SUBDIRECTOR DE OBRA
    nombre_subdirector_obra = fields.Char(string="Nombre:", required=True)
    puesto_subdirector_obra = fields.Char(string="Puesto:", required=True)
    # RESPONSABLE / LICITACIONES
    nombre_responsable_licitacion = fields.Char(string="Nombre:", required=True)
    puesto_responsable_licitacion = fields.Char(string="Puesto:", required=True)
    # FIRMAS DE CONTRATOS
    nombre_testigo_uno = fields.Char(string="Nombre testigo uno:", required=True)
    puesto_testigo_uno = fields.Char(string="Puesto testigo uno:", required=True)
    nombre_testigo_dos = fields.Char(string="Nombre testigo dos:", required=True)
    puesto_testigo_dos = fields.Char(string="Puesto testigo dos:", required=True)
    nombre_testigo_tres = fields.Char(string="Nombre testigo tres:", required=True)
    puesto_testigo_tres = fields.Char(string="Puesto testigo tres:", required=True)

