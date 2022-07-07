from odoo import models, fields, api


class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    abk_uom_class_id = fields.Char('UOM Class')
    abk_ium = fields.Char('Inventory UoM')
    abk_sales_um = fields.Char('Sales UM')
    abk_purchase_UM = fields.Char('Purchase UM')
    abk_prod_code = fields.Char('Group')
    abk_class_id = fields.Many2one("abk.product.class", string='Product Class')
    abk_commodity_code = fields.Many2one("abk.hscommodity", string='HS Commodity')
    abk_on_hold = fields.Char('Hold')
    abk_on_hold_date = fields.Char('Hold Date')
    abk_on_hold_reason_code = fields.Char('Hold Reason Code')
    abk_track_dimension = fields.Char('Track Dimension UOMs')
    abk_non_stock = fields.Char('Non-Stock Item')
    abk_mfg_comment = fields.Char('Manufacturing Comment')
    abk_pur_comment = fields.Char('Purchase Comment')
    abk_brand = fields.Many2one("abk.brand", string='Brand')
    abk_sub_brand = fields.Many2one("abk.brand", string='Sub-Brand')
    abk_co_warehouse = fields.Char('CO Warehouse')
    abk_grs_weight = fields.Float('GRS Weight(g)')
    abk_fsc_paper_weight = fields.Char('FSC Paper Weight (kg)')
    abk_fsc_claim = fields.Many2one("abk.fscclaim",string='FSC Claim')
    abk_agent = fields.Many2one("res.partner", string='Agent')
    abk_fk_lookup = fields.Char('F/K Lookup')
    abk_wo_salesman = fields.Many2one("res.users", string='WO Salesman')
    abk_plant = fields.Char('Site')
    abk_prim_whse = fields.Char('Primary Warehouse')
    abk_minimum_qty = fields.Integer('Min On-Hand')
    abk_maximum_qty = fields.Integer('Max On-Hand')
    abk_safety_qty = fields.Char('Safety Stock')
    abk_reorder_level = fields.Integer('Re-Order to Max')
    abk_minorder_qty = fields.Integer('Min Order Qty')
    abk_lead_time = fields.Datetime('Lead Time')
    abk_production_lead_time = fields.Datetime('Production Lead Time')
    abk_generate_sugg = fields.Char('Generate PO Suggestions')
    abk_backflush = fields.Char('BackFlush')
    abk_prim_bin_num = fields.Char('Bin')

    abk_part_length = fields.Float('Part Length')
    abk_part_height = fields.Float('Part Height')
    abk_part_width = fields.Float('Part Width')

    # existing
    abk_part_num = fields.Char('Part')
    abk_part_description = fields.Text('Product Description')
    abk_type_code = fields.Char('Type')

    # add fields import product
    abk_custno = fields.Char('Customer No')
    abk_custsname = fields.Char('Customer Name')
    abk_infordate = fields.Datetime('Infor Date')
    abk_sizew1 = fields.Char('Size W1')
    abk_sizew2 = fields.Char('Size W2')
    abk_sizew = fields.Char('Size W')
    abk_sizel = fields.Char('Size L')
    abk_sizel1 = fields.Char('Size L1')
    abk_sizel2 = fields.Char('Size L2')
    abk_sizeunit = fields.Char('Size Unit')
    abk_itemsize = fields.Char('Item Size')
    abk_type1 = fields.Char('Type 1')
    abk_type2 = fields.Char('Type 2')
    abk_type3 = fields.Char('Type 3')
    abk_type4 = fields.Char('Type 4')
    abk_type5 = fields.Char('Type 5')
    abk_stockamt = fields.Char('Stock Amount')
    abk_unit = fields.Char('Unit')
    abk_producttype = fields.Char('Product Type')
    abk_adgetype = fields.Char('Adge Type')
    abk_machine = fields.Char('Machine')
    abk_process = fields.Char('Process')
    abk_paper = fields.Char('Paper')
    abk_fcolourno = fields.Char('Fcolour No')
    abk_fcolour = fields.Char('Fcolour')
    abk_bcolourno = fields.Char('Bcolour No')
    abk_bcolour = fields.Char('Bcolour')
    abk_trimsize1 = fields.Char('Trimsize1')
    abk_trimsize2 = fields.Char('Trimsize2')
    abk_trimunit = fields.Char('Trimunit')
    abk_remake = fields.Char('Remake')
    abk_remake2 = fields.Char('Remake 2')

    abk_internal_price = fields.Monetary(string="Internal Price")
    abk_tax_category = fields.Char(string="TaxCloud Category")
    abk_co_created = fields.Boolean(string="CO Created")
    abk_manufacturer = fields.Many2one("mrp.production", string="Manufacturer")
    abk_country_of_origin = fields.Many2one('res.country', string='Country of Origin')
    abk_supp_unit_factor = fields.Float(string="Supplier Units Factor")
    abk_partial_completed = fields.Char(string="Partial Completed")
    abk_inventory = fields.Char(string="Inventory")
    abk_shelf_life_days = fields.Integer(string="Shelf Life / Days")
    abk_run_out = fields.Boolean(string="Run Out")
    abk_web_saleable = fields.Boolean(string="Web Saleable")
    abk_use_part_rev = fields.Boolean(string="Use part rev")
    abk_constrained_material = fields.Boolean(string="Constrained Material")
    abk_track_lots = fields.Boolean(string="Track Lots")
    abk_package_control_specific_uoms = fields.Boolean(string="Package Control Specific UoMs")
    abk_track_multiple_uoms = fields.Boolean(string="Track Multiple UoMs")
    abk_track_serial_numbers = fields.Boolean(string="Track Serial numbers")
    abk_consolidated_purchasing = fields.Boolean(string="Consolidated purchasing")
    abk_receipt_docs_required = fields.Boolean(string="Receipt docs Required")
    abk_shipping_docs_required = fields.Boolean(string="Shipping docs required")
    abk_link_to_contract = fields.Boolean(string="Link to contract")
    abk_mdpv = fields.Integer(string="MDPV")
    abk_returnable_container = fields.Integer(string="Returnable Container")
    abk_fk_number = fields.Char(string='F/K Number')
    abk_warranty = fields.Many2one("abk.warranty", string='Warranty')
    abk_head_asm_analysis = fields.Many2one("abk.head.analysis", string='Head/Asm analysis')
    abk_material_analysis = fields.Many2one("abk.material.analysis", string='Material Analysis')
    abk_reference_category = fields.Many2one("abk.reference.category", string='Reference Category')
    abk_rpd_part = fields.Char(string="RPD Part")
    abk_global = fields.Boolean(string="Global")
    abk_inactive = fields.Boolean(string="Inactive")
    abk_important = fields.Many2one("abk.important", string="Important")
    abk_sortkey1 = fields.Char(string="SortKey1")
    abk_sortkey2 = fields.Char(string="SortKey2")
    abk_sortkey3 = fields.Char(string="SortKey3")
    abk_sortkey4 = fields.Char(string="SortKey4")


class ABKProductClass(models.Model):
    _name = 'abk.product.class'
    _description = 'Product Class'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKWarranty(models.Model):
    _name = 'abk.warranty'
    _description = 'Warranty'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKHeadAsmAnalysis(models.Model):
    _name = 'abk.head.analysis'
    _description = 'Head/Asm Analysis'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKMaterialAnalysis(models.Model):
    _name = 'abk.material.analysis'
    _description = 'Material Analysis'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKReferenceCategory(models.Model):
    _name = 'abk.reference.category'
    _description = 'Reference Category'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKHSCommodity(models.Model):
    _name = 'abk.hscommodity'
    _description = 'HS Commodity'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKFSCClaim(models.Model):
    _name = 'abk.fscclaim'
    _description = 'FSC Claim'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKImportant(models.Model):
    _name = 'abk.important'
    _description = 'Important'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)

