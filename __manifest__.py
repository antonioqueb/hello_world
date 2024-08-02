# hello_world/__manifest__.py
{
    'name': 'Hello World',
    'version': '1.0',
    'summary': 'Módulo de ejemplo Hello World',
    'sequence': -100,
    'description': """Módulo de ejemplo para mostrar 'Hello World'""",
    'category': 'Uncategorized',
    'author': 'Alphaqueb',
    'website': 'http://www.tuwebsite.com',
    'depends': ['base'],
    'data': [
        'views/hello_world_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
