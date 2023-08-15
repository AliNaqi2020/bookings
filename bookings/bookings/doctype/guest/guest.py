# Copyright (c) 2023, Ali % Arsalan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe.model.document import Document


class Guest(Document):
    def validate(self):
        self.validate_dates()

    def validate_dates(self):
        if self.check_in_date and self.check_out_date and self.check_in_date >= self.check_out_date:
            frappe.throw('Check-out date must be after check-in date')

        if self.payment_status == 'Paid' and self.total_amount <= 0:
            frappe.throw(
                'Total amount must be greater than zero for paid bookings')
