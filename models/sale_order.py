from odoo import models, fields

class SaleOrder(models.Model):
    _inherit='sale.order'
    
    payment_type=fields.Char("Payment Type")