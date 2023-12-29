from datetime import date
from odoo import models, fields, api

class School(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    attachment = fields.Binary(string="Attachment")
    image = fields.Image(string="Image")
    name = fields.Many2one('res.partner', string="Student", required=True)
    date_of_birth = fields.Date(string="DOB")
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True, readonly=True)
    gender = fields.Selection(string="Gender", selection=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    standard = fields.Integer(string="Standard")
    section = fields.Selection(string="Section", selection=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    subject_ids = fields.One2many('school.subject', 'school_student', string='Subject')
    # Student Personal Information
    father = fields.Char(string="Father")
    mother = fields.Char(string="Mother")
    father_occupation = fields.Text(string="FatherOccupation")
    mother_occupation = fields.Text(string="MotherOccupation")
    sibling = fields.Boolean(string='Sibling')
    address = fields.Text(string="Address")
    # Result
    first_sem = fields.Float(string='FirstSem')
    second_sem = fields.Float(string='SecondSem')
    Third_sem = fields.Float(string='ThirdSem')
    percentage = fields.Float(compute="_calc_per", store=True)
    sum = fields.Integer(string="Sum", compute="_compute_sum")

    @api.depends('subject_ids.number')
    def _compute_sum(self):
        s = 0
        for record in self:
            for rec in record.subject_ids:
                s += rec.number
        self.sum = s

    @api.depends('first_sem', 'second_sem', 'Third_sem')
    def _calc_per(self):
        self.percentage = (self.first_sem + self.second_sem + self.Third_sem) / 3
    @api.depends('age')
    def _compute_age(self):
        today = date.today()
        self.age = today.year - self.date_of_birth.year

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject Student'

    name = fields.Char(string="SubjectName")
    school_student = fields.Many2one('school.student', string="SchoolStudent")
    code = fields.Char(string="Subject Code")
    number = fields.Integer(string="Number")

