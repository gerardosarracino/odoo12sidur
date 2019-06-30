# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions
import odoorpc


class FirmasLogos(models.Model):
    _name = 'firmas_logos.firmas_logos'
    # _inherit = 'res.partner'



    '''@api.one
    def consulta(self):
        odoo = odoorpc.ODOO('localhost', port=1269)

        # Check available databases
        print(odoo.db.list())

        # Login
        odoo.login('odoo12', 'sarracino1hvesp@gmail.com', 'admin')

        db = odoo.env['firmas_logos_firmas_logos']
        busqueda = db.browse(1)
        a = busqueda.name
        return a'''

    '''@api.multi
    def consulta(self):
        SQL = 'select name from firmas_logos_firmas_logos'
        self.env.cr.execute(SQL)
        for row in self.env.cr.fetchall():
            return row'''

    '''@api.multi
    def write(self, values, data):
        res = super(FirmasLogos, self).write(values, data)
        if values.get(''):
            self.()
        return res'''

    #  default=lambda self: self.consulta()
    @api.model
    def create(self, values):
        # res = super(FirmasLogos, self).create(values)
        limit = len(self.search([]))
        if limit >= 1:
            raise exceptions.Warning('Ya se tienen datos creados')
        else:
            return super(FirmasLogos, self).create(values)

    # MUNICIPIO ?
    select = [('sidur', 'SIDUR')]
    municipio = fields.Selection(select, string="Municipio:", default="sidur" )
    # DEPENDENCIA INSTITUCION
    name = fields.Char(string="Nombre:", )
    image = fields.Binary("Image", help="This field holds the image used as avatar for ")
    declaraciones_dependencia = fields.Text(string="Declaraciones Dependencia:",)
    titular = fields.Char(string="Titular:", )
    domicilio = fields.Text(string="Domicilio:", )
    # TITULAR
    nombre_titular = fields.Char(string="Nombre:",)
    puesto_titular = fields.Char(string="Puesto:", )
    fecha_nombramiento_titular = fields.Date(string="Fecha de Nombramiento:", )
    # CONTRALORIA INTERNA
    nombre_contraloria = fields.Char(string="Representante:", )
    puesto_contraloria = fields.Char(string="Puesto:", )
    fecha_nombramiento_contraloria = fields.Date(string="Fecha Nombramiento:", )
    # REPRESENTANTE CIUDADANO
    nombre_representante_ciudadano = fields.Char(string="Nombre:", )
    puesto_representante_ciudadano = fields.Char(string="Puesto:", )
    # DIRECTOR / COORDINADOR ADMINISTRATIVO
    nombre_coordinador_administrativo = fields.Char(string="Nombre:", )
    puesto_coordinador_administrativo = fields.Char(string="Puesto:", )
    # DIRECTOR / COORDINADOR PLANEACION
    nombre_coordinador_planeacion = fields.Char(string="Nombre:", )
    puesto_coordinador_planeacion = fields.Char(string="Puesto:", )
    # DIRECTOR / COORDINADOR JURIDICO
    nombre_coordinador_juridico = fields.Char(string="Nombre:", )
    puesto_coordinador_juridico = fields.Char(string="Puesto:", )
    # RESPONSABLE / SUBDIRECTOR DE OBRA
    nombre_subdirector_obra = fields.Char(string="Nombre:", )
    puesto_subdirector_obra = fields.Char(string="Puesto:", )
    # RESPONSABLE / LICITACIONES
    nombre_responsable_licitacion = fields.Char(string="Nombre:", )
    puesto_responsable_licitacion = fields.Char(string="Puesto:", )
    # FIRMAS DE CONTRATOS
    nombre_testigo_uno = fields.Char(string="Nombre testigo uno:", )
    puesto_testigo_uno = fields.Char(string="Puesto testigo uno:", )
    nombre_testigo_dos = fields.Char(string="Nombre testigo dos:", )
    puesto_testigo_dos = fields.Char(string="Puesto testigo dos:", )
    nombre_testigo_tres = fields.Char(string="Nombre testigo tres:", )
    puesto_testigo_tres = fields.Char(string="Puesto testigo tres:", )

