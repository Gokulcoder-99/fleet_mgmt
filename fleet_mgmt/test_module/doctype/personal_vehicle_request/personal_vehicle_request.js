// Copyright (c) 2023, Gokul and contributors
// For license information, please see license.txt
frappe.ui.form.on('Personal_Vehicle_Request', {
	refresh: function(frm) {
		const req= frm.doc
		frappe.db.get_list('Details_Of_Vehicles', {
			fields: ['vehicle_no', 'seating_capacity'],
		}).then(records => {
			const start = frm.doc.start_date_and_time;
			const end = frm.doc.end_date_and_time;
			records.filter(i=>{
				

				//return vehicleEndTime <= start || vehicleStartTime >= end;
			})
			
		})
		
	 }
});

frappe.ui.form.on('Personal_Vehicle_Request', 'end_date_and_time', function(frm) {
    
});
