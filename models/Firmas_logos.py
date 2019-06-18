# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Municipio(models.Model):
    _name = 'firmas_logos.municipio'

    select = [('sidur', 'SIDUR')]
    # sidur no es un municipio, pero asi aparece en el cronograma y en sidur, verificar verdadero nombre del campo
    name = fields.Selection(select, string="Municipio:", required=True)


class DependenciaInstitucion(models.Model):
    _name = 'firmas_logos.dependencia_institucion'

    name = fields.Char(string="Nombre:", required=True)
    image = fields.Binary("Image", help="This field holds the image used as avatar for ")
    # in xml, <field name="image" widget='image' class="oe_avatar"/>
    declaraciones_dependencia = fields.Text(string="Declaraciones Dependencia:", required=True)
    titular = fields.Char(string="Titular:", required=True)
    domicilio = fields.Text(string="Domicilio:", required=True)


class Titular(models.Model):
    _name = 'firmas_logos.titular'

    name = fields.Char(string="Nombre:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)
    fecha_nombramiento = fields.Date(string="Fecha de Nombramiento:", required=True)
# contraloria interna no aparece en el cronograma de actividades pero en sidur si, PENDIENTE


class ContraloriaInterna(models.Model):
    _name = 'firmas_logos.contraloria_interna'

    name = fields.Char(string="Representante:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)
    fecha_nombramiento = fields.Date(string="Fecha Nombramiento:", required=True)


class RepresentanteCiudadano(models.Model):
    _name = 'firmas_logos.representante_ciudadano'

    name = fields.Char(string="Nombre:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)


class DirectorCoordinadorAdministrativo(models.Model):
    _name = 'firmas_logos.director_coordinador_administrativo'

    name = fields.Char(string="Nombre:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)


class DirectorCoordinadorPlaneacion(models.Model):
    _name = 'firmas_logos.director_coordinador_planeacion'

    name = fields.Char(string="Nombre:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)


class DirectorCoordinadorJuridico(models.Model):
    _name = 'firmas_logos.director_coordinador_juridico'

    name = fields.Char(string="Nombre:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)


class ResponsableSubdirectorObra(models.Model):
    _name = 'firmas_logos.responsable_subdirector_obra'

    name = fields.Char(string="Nombre:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)


class ResponsableLicitaciones(models.Model):
    _name = 'firmas_logos.responsable_licitaciones'

    name = fields.Char(string="Nombre:", required=True)
    puesto = fields.Char(string="Puesto:", required=True)


class FirmasContratos(models.Model):
    _name = 'firmas_logos.firmas_contratos'

    name = fields.Char(string="Nombre testigo uno:", required=True)
    puesto_testigo_uno = fields.Char(string="Puesto testigo uno:", required=True)
    nombre_testigo_dos = fields.Char(string="Nombre testigo dos:", required=True)
    puesto_testigo_dos = fields.Char(string="Puesto testigo dos:", required=True)
    nombre_testigo_tres = fields.Char(string="Nombre testigo tres:", required=True)
    puesto_testigo_tres = fields.Char(string="Puesto testigo tres:", required=True)