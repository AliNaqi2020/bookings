// Copyright (c) 2023, Ali % Arsalan and contributors
// For license information, please see license.txt


// myapp/myapp/doctype/guest/guest.js

frappe.ui.form.on('Guest', {
    refresh: function(frm) {
        // Your custom client-side logic here
        // For example, you can show/hide fields based on conditions
    },

    calculateTotalAmount: function(frm) {
        // Calculate the total amount based on payment method and other fields
        if (frm.doc.payment_method === 'Credit Card') {
            frm.set_value('total_amount', frm.doc.room_rate * frm.doc.nights);
        }
    }
});
