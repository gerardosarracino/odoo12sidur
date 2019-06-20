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
        'security/ir.model.access.csv', #Permisos de usuarios
        'views/generales/generales.xml', #Vista de generales y origenes de obra
        'views/generales/tipo_obra.xml', #Vista de tipos de obra pertenece a generales
        'views/generales/municipios.xml', #Vista de municipios pertenece a generales
        'views/generales/programas_inversion.xml', #Vista de programas de inversion pertenece a generales
        'views/generales/modalidades.xml', #Vista de modalidades pertenece a generales
        'views/generales/parametros.xml', #Vista de parametros pertenece a generales
        'views/generales/deducciones.xml', #Vista de deducciones pertenece a generales
        'views/generales/evaluacion_puntos.xml', #Vista de evaluacion de puntos pertenece a generales
        'views/generales/apartados_proyecto.xml', #Vista de apartados de proyectos pertenece a generales
        'views/generales/etapas_pago.xml', #Vista de etapas de pagos pertenece a generales
        'views/generales/estados.xml', #Vista para agregar estados de la republica pertenece a generales
        'views/firmas_logos/firmas_logos.xml', #Vista firmas/logos
        'views/contratistas/contratista.xml', #Vista de contratistas
        'views/plantillas/plantillas.xml', #Vista de plantillas
        'views/control_expediente/control_expediente.xml' #Vista de control de expediente
    ],

    'installable': True,
}