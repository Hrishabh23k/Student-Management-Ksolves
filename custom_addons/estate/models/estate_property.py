from odoo import fields, models

class Estate(models.Model):
    _name = 'estate.property'
    _description = 'The real estate property model'

    name = fields.Char(string='Name')
    desc = fields.Text(string='Description')
    postcode = fields.Char(string='PostCode')
    date_availability = fields.Date(string="Date_Availability")
    expected_price = fields.Float(string="Expected_Price")
    selling_price = fields.Float(string="Selling_Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living_Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden_Area")
    garden_orientation = fields.Selection(string="Garden_orientation", selection=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')])
