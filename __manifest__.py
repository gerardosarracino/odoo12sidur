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
        'views/Generales/Generales.xml',
        'views/Tipo_obra.xml',
        'views/municipios.xml',
        'views/programas_inversion.xml',
        'views/Modalidades.xml',
        'views/parametros.xml',
        'views/deducciones.xml',
        'views/evaluacion_puntos.xml',
        'views/apartados_proyecto.xml',
        'views/etapas_pago.xml'
    ],

    'installable': True,
}