// Copyright (c) 2023, Ali % Arsalan and contributors
// For license information, please see license.txt


frappe.ui.form.on('Reservation', {
    check_in: function(frm) {
        calculateNights(frm);
    },
    check_out: function(frm) {
        calculateNights(frm);
    }
});

function calculateNights(frm) {
    console.log("Testing.....");
    
    if (frm.doc.check_in && frm.doc.check_out) {
        var checkInDate = new Date(frm.doc.check_in);
        var checkOutDate = new Date(frm.doc.check_out);
        var timeDiff = checkOutDate - checkInDate;
        var nights = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
        frm.set_value('nights', nights);
    }
    console.log("Testing.....");
}

// Testing Commit
// Second Commit
