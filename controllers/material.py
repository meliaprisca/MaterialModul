import odoo

from odoo import http, models, fields, _
from odoo.http import request
import json

# class KedaMaterial(http.Controller):
#     @http.route('/web/material/list', type='http', website=True)
#     def get_sale_list(self, **kwargs):
#         orders = request.env['keda.material'].sudo().search([])
#         data = {
#             'orders' : orders 
#         }
#         return request.render('keda.website_material_list', data)
    
class LatihanControllerDua(http.Controller):
    @http.route('/material/list', type='http')
    def get_sale_list(self, **kwargs):
        orders = request.env['keda.material'].sudo().search([])
        data = {
            'orders' : orders
        }
        return request.render('keda.sale_list', data)

    @http.route('/web/material/list', type='http', website=True)
    def get_web_sale_list(self, **kwargs):
        orders = request.env['keda.material'].sudo().search([])
        data = {
            'orders' : orders 
        }
        return request.render('keda.website_material_list', data)