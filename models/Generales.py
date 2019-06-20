# -*- coding: utf-8 -*-

from odoo import models, fields


class OrigenesObra(models.Model):
    _name = 'generales.origenes_obra'

    name = fields.Char(string="Nombre:", required=True)
    observaciones = fields.Text(string="Observaciones:", required=True)


class TipoObra(models.Model):
    _name = 'generales.tipo_obra'

    name = fields.Char(string="Nombre:", required=True)


class Estados(models.Model):
    _name = 'generales.estado'

    name = fields.Char(string="Estado", required=True)
    municipios = fields.One2many("generales.municipios", "name")
    generales = fields.One2many("generales.parametros", "estado")


class Municipios(models.Model):
    _name = 'generales.municipios'

    name = fields.Many2one('generales.estado', string="Entidad Federativa: ", required=True)
    municipio_delegacion = fields.Char(string="Municipio/Delegación: ", required=True)
    clave_municipio = fields.Integer(string="Clave municipio/Delegación: ", required=True)


class ProgramasInversion(models.Model):
    _name = 'generales.programas_inversion'

    name = fields.Char(string="nombre", required=True)
    clave = fields.Char(string="Clave:", required=True)
    select = [('federal', 'FEDERAL'), ('estatal', 'ESTATAL')]
    normatividad = fields.Selection(select, string="Normatividad:", required=True, default="federal")


class Modalidades(models.Model):
    _name = 'generales.modalidades'

    name = fields.Many2one('generales.programas_inversion', inverse_name="name", string="Programas de inversión:",
                           required=True)
    categoria_programatica = fields.Text(string="Categoría Programática:", required=True)


class Parametros(models.Model):
    _name = 'generales.parametros'

    lema = fields.Text(string="Lema del Año:", required=True, default="2017: CENTENARIO DE LA CONSTITUCIÓN, PACTO "
                                                                      "SOCIAL SUPREMO DE LOS MEXICANOS")
    iva = fields.Float(string="% IVA", required=True, default="0.16")
    retencion = fields.Float(string="% Retención:", required=True, default="0.02")
    select = [('diario', 'DIARIO'), ('mensual', 'MENSUAL')]
    periodicidad_retencion = fields.Selection(select, string="Periodicidad Retención:", required=True,
                                              default="mensual")
    sancion = fields.Float(string="% Sanción:", required=True, default="0.03")
    periodicidad_sancion = fields.Selection(select, string="Periodicidad Sanción:", default="mensual")

    estado = fields.Many2one('generales.estado', string="Estado:", required=True)

    lugar_licitacion = fields.Text(string="Lugar Actos Licitación:", required=True, default="SALA DE JUNTAS")


class Deducciones(models.Model):
    _name = 'generales.deducciones'

    name = fields.Char(string="Deducción:", required=True)
    porcentaje = fields.Float(string="Porcentaje:", required=True)


class EvaluacionPuntos(models.Model):
    _name = 'generales.evaluacion'

    select = [('1', 'CALIDAD EN LA OBRA'), ('2', 'CAPACIDAD DEL LICITANTE'),
              ('3', 'EXPERIENCIA Y ESPECIALIDAD DEL LICITANTE'), ('4', 'PROPUESTA ECONÓMICA')]
    name = fields.Selection(select, string="Rubro:", required=True, default="1")
    clave = fields.Char(string="Clave:", required=True)
    sub_rubro = fields.Char(string="SubRubro:", required=True)
    solicitado = fields.Text(string="Solicitado en:", required=True)


class ApartadosProyecto(models.Model):
    _name = 'generales.apartados_proyectos'

    name = fields.Char(string="Nombre del apartado:", required=True)


class EtapasPago(models.Model):
    _name = 'generales.etapas_pago'

    name = fields.Char(string="Etapas de pagos", required=True)
    etapa = fields.Boolean(string="Etapa pago", required=True)

