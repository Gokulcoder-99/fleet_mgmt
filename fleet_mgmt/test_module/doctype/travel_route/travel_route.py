# Copyright (c) 2023, Gokul and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class TravelRoute(Document):
	# pass
	def validate(self):
		self.qr_generator=f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={self.emp_id}/{self.route_id}"
	                                              