# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OrigenesObra(models.Model):
    _name = 'generales.origenes_obra'

    name = fields.Char(string="Nombre", required=True)
    observaciones = fields.Text(string="Observaciones", required=True)


class TipoObra(models.Model):
    _name = 'generales.tipo_obra'

    name = fields.Char(string="Nombre", required=True)


class Municipios(models.Model):
    _name = 'generales.municipios'

    estados = [
                  ('AGC', "Aguascalientes"),
                  ('BCN', "Baja California Norte"),
                  ('BCS', "Baja California Sur"),
                  ('CAMP', "Campeche"),
                  ('CHI', "Chiapas"),
                  ('CHIH', "Chihuahua"),
                  ('COA', "Coahuila"),
                  ('COL', "Colima"),
                  ('DF', "Distrito Federal"),
                  ('DUR', "Durango"),
                  ('EM', "Estado de Mexico"),
                  ('GTO', "Guanajuato"),
                  ('GRO', "Guerrero"),
                  ('HDO', "Hidalgo"),
                  ('JCO', "Jalisco"),
                  ('MCH', "Michoacan"),
                  ('MRO', "Morelos"),
                  ('NR', "Nayarit"),
                  ('NLN', "Nuevo Leon"),
                  ('OXC', "Oaxaca"),
                  ('PUE', "Puebla"),
                  ('QRT', "Queretaro"),
                  ('QTR', "Quintana Roo"),
                  ('SNL', "San Luis Potosi"),
                  ('SIN', "Sinaloa"),
                  ('SONORA', "Sonora"),
                  ('TBC',"Tabasco"),
                  ('TMP', "Tamaulipas"),
                  ('TXL', "Tlaxcala"),
                  ('VER', "Veracruz"),
                  ('YCT', "Yucatan"),
                  ('ZAC', "Zacatecas")
                  ]
    # falta relacion One2many de entidad_federativa duda
    name = fields.Selection(estados, string="Entidad Federativa: ", default="SONORA", required=True)
    municipio_delegacion = fields.Char(string="Municipio/Delegacion: ", required=True)
    clave_municipio = fields.Integer(string="Clave municipio/Delegacion: ", required=True)


class ProgramasInversion(models.Model):
    _name = 'generales.programas_inversion'

    # falta relacion One2many de Nombre
    name = fields.Char(string="Nombre:", required=True)

    clave = fields.Char(string="Clave:", required=True)
    select = [('FEDERAL', 'FEDERAL'), ('ESTATAL', 'ESTATAL')]
    normatividad = fields.Selection(select, string="Normatividad:", required=True, default="FEDERAL")


class Modalidades(models.Model):
    _name = 'generales.modalidades'
    # relaciones falta
    name = fields.Many2one('generales.programas_inversion', 'Programas de inversion:', ondelete="cascade"
                                          , required=True)
    categoria_programatica = fields.Text(string="Categoría Programática:", required=True)


class Parametros(models.Model):
    _name = 'generales.parametros'

    lema = fields.Text(string="Lema del Año:", required=True, default="2017: CENTENARIO DE LA CONSTITUCIÓN, PACTO "
                                                                      "SOCIAL SUPREMO DE LOS MEXICANOS")
    iva = fields.Float(string="% IVA", required=True, default="16")
    retencion = fields.Float(string="% Retención:", required=True, default="2")
    select = [('DIARIO', 'DIARIO'), ('MENSUAL', 'MENSUAL')]
    periodicidad_retencion = fields.Selection(select, string="Periodicidad Retención:", required=True,
                                              default="MENSUAL")
    sancion = fields.Float(string="% Sanción:", required=True, default="3")
    periodicidad_sancion = fields.Selection(select, string="Periodicidad Sanción:", default="MENSUAL")
    estado = fields.Many2one('generales.municipios', 'Estado:', required=True)
    lugar_licitacion = fields.Text(string="Lugar Actos Licitación:", required=True, default="SALA DE JUNTAS")


class Deducciones(models.Model):
    _name = 'generales.deducciones'

    name = fields.Char(string="Deduccion:", required=True)
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

