# Copyright (c) 2024, kelvin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Sale(Document):
	pass




def create_inventory_transaction_on_sale(doc, method):
    for item in doc.items:
        inventory_transaction = frappe.new_doc("Inventory Transaction")
        inventory_transaction.product = item.product
        inventory_transaction.quantity = item.quantity
        inventory_transaction.transaction_type = "OUT"
        inventory_transaction.insert()
        inventory_transaction.submit()