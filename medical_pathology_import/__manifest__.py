# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

{
    'name': 'Medical Pathology - Import Interface',
    'summary': 'Provides an interface for medical pathology data imports',
    'version': '10.0.1.0.0',
    'category': 'Technical Settings',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'GPL-3',
    'depends': [
        'medical_pathology',
    ],
    'data': [
        'wizards/medical_pathology_import.xml',
    ],
    'installable': True,
}
