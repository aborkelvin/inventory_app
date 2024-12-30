# Copyright (c) 2024, kelvin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class InventoryTransaction(Document):
	pass


def update_product_quantity(doc, method):
    print("I'm running, product update is running please")
    frappe.msgprint(f"Updating product: {doc.product} with quantity: {doc.quantity}")
    
    product = frappe.get_doc("Product", doc.product)
    
    if doc.transaction_type == "IN":
        product.quantity += doc.quantity
        frappe.msgprint(f"Product {product.name} updated successfully. New quantity: {product.quantity}")
    
    elif doc.transaction_type == "OUT":
        if product.quantity >= doc.quantity:
            product.quantity -= doc.quantity
            frappe.msgprint(f"Product {product.name} updated successfully. New quantity: {product.quantity}")
        else:
            # Show message before throwing exception
            frappe.msgprint("Not enough stock to complete this transaction.", alert=True)
            frappe.throw("Not enough stock to complete this transaction.")
    
    product.save()
   
    



""" 
def update_product_quantity(doc, method):
    print("I'm running, product update is running please")
    frappe.msgprint(f"Updating product: {doc.product} with quantity: {doc.quantity}")
    if doc.transaction_type == "IN":
        product = frappe.get_doc("Product", doc.product)
        # Update quantity using update method
        product.update({"quantity": product.quantity + doc.quantity})
    elif doc.transaction_type == "OUT":
        product = frappe.get_doc("Product", doc.product)
        if product.quantity >= doc.quantity:
            # Update quantity using update method
            product.update({"quantity": product.quantity - doc.quantity})
        else:
            frappe.throw("Not enough stock to complete this transaction.") """