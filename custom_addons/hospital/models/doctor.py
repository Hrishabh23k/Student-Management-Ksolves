from odoo import fields, models

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'name of doctors'

    doctor_id = fields.Integer(string='DoctorId')
    doctor_name = fields.Many2one('res.partner', string="DoctorName")
