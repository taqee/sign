# Copyright 2025 Kencove - Mohamed Alkobrosli
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sign OCA Font Support",
    "version": "18.0.1.0.0",
    "summary": "Adds Arabic/Persian font support for Sign OCA reports using ReportLab",
    "description": """
        This module enables proper Arabic text rendering in PDFs generated
        by the Sign OCA module using arabic-reshaper and python-bidi.
    """,
    "category": "Tools",
    "author": "Kencove",
    "maintainers": ["Kencove"],
    "depends": ["sign_oca"],
    "external_dependencies": {
        "python": [
            "arabic-reshaper",
            "python-bidi",
            "reportlab",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
