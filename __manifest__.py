{
    'name': "Sale_Ship",

    'summary': "manage ship",

    'description': """
         saleship module for managing ship 
    
    
    
    
    """,

    'author': "Binoy",
    'website': "binoyship@gmail.com",

    'category': 'Test',
    'version': '0.1',

    'depends' : ['sale','sale_management'],



    'data':[

       'views/sale_ship_view.xml',
       'views/sale_order_view.xml',
       'views/purchase_order_view.xml',
       'views/ship_stock_picking.xml',
       'views/sale_ship_details.xml',
       'wizard/ship_wizard_view.xml',
       'views/sale_ship_account.xml',
       'report/report.xml',
       'report/report_invoice.xml',
       'report/report_delivery.xml',
       'report/sale_report_view.xml',
       'data/ir_sequence_data.xml',
],

}
