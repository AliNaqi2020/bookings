# Copyright (c) 2023, Ali % Arsalan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Reservation(Document):
	
	def validate(doc, method):
		if doc.check_in and doc.check_out:
			if doc.check_in >= doc.check_out:
				frappe.throw('Check-out date must be after check-in date')

			if doc.status == 'Confirmed':
				doc.status = 'Checked In'
				doc.save()  # Save the updated document
			elif doc.status == 'Checked In' and doc.check_out <= frappe.utils.today():
				doc.status = 'Checked Out'
				doc.save()  # Save the updated document


			def get_reservation():
						# Create a new Reservation document
						new_reservation = frappe.new_doc("Reservation")
						new_reservation.check_in = "2023-08-15"
						new_reservation.check_out = "2023-08-20"
						new_reservation.status = "Confirmed"

						# Insert the document
						new_reservation.insert()

						# Call the validate function during the 'insert' method
						new_reservation.run_method("validate", method="insert")

						# Update the document's status
						new_reservation.status = "Checked In"

						# Save the document
						new_reservation.save()

						# Call the validate function during the 'save' method
						new_reservation.run_method("validate", method="save")

						# Submit the document
						new_reservation.submit()

						# Call the validate function during the 'submit' method
						new_reservation.run_method("validate", method="submit")
