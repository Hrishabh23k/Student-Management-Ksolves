from odoo import fields, models


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'name of patient'

    name = fields.Many2one('res.partner', string="Name")
    description = fields.Text(string="Description")
    doctor_name = fields.Many2one('hospital.doctor', string="DoctorName")
