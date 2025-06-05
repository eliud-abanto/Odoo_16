# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesor(models.Model):
    _name = 'escuela.profesor'

    name = fields.Char(string="Nombre", required=True)
    last_name = fields.Char(string="Apellido", required=True)
    career = fields.Char(string="Profesion", required=True)
    aula = fields.Many2many("escuela.aula", string="aula")


class estudiante(models.Model):
    _name = 'escuela.estudiante'

    name = fields.Char(string="Nombre", required=True)
    last_name = fields.Char(string="Apellido", required=True)
    birth = fields.Date(string="Fecha de nacimiento", required=True)
    aula = fields.Many2one("escuela.aula", string="aula")

class aula(models.Model):
    _name = 'escuela.aula'

    name = fields.Char(string="Numeral", required=True)
    seccion = fields.Selection(
        [
            ("a", "A"),
            ("b", "B"),
            ("c", "C"),
        ],
        string="Seccion",
        default="a",
        required=True,
    )
    capacity = fields.Integer(string="Capacidad de estudiantes")
    student = fields.One2many("escuela.estudiante", inverse_name="aula", string="Estudiante(s)")
    teacher = fields.Many2many("escuela.profesor", string="Profesor(es)")

    def name_get(self):
        result = []
        for record in self:
            display_name = f"{record.name} - Sección {record.seccion.upper()}"
            result.append((record.id, display_name))
        return result


class materia(models.Model):
    _name = 'escuela.materia'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripcion")
    aula = fields.Many2many("escuela.aula", string="aula")

    