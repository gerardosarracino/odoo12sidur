# -*- coding: utf-8 -*-
{
    'name': "informacion_basica",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/generales/Generales.xml',
        'views/generales/Tipo_obra.xml',
        'views/generales/municipios.xml',
        'views/generales/programas_inversion.xml',
        'views/generales/Modalidades.xml',
        'views/generales/parametros.xml',
        'views/generales/deducciones.xml',
        'views/generales/evaluacion_puntos.xml',
        'views/generales/apartados_proyecto.xml',
        'views/generales/etapas_pago.xml',
        'views/generales/estados.xml',
        'views/firmas_logos/dependencia_institucion.xml',
        'views/firmas_logos/titular.xml',
        'views/firmas_logos/contraloria_interna.xml',
        'views/firmas_logos/representante_ciudadano.xml',
        'views/firmas_logos/director_coordinador_administrativo.xml',
        'views/firmas_logos/director_coordinador_planeacion.xml',
        'views/firmas_logos/director_coordinador_juridico.xml',
        'views/firmas_logos/responsable_subdirector_obra.xml',
        'views/firmas_logos/responsable_licitaciones.xml',
        'views/firmas_logos/firmas_contratos.xml'
    ],

    'installable': True,
}