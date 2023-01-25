// Copyright (c) 2023, Ahmed Al-farran and contributors
// For license information, please see license.txt

frappe.ui.form.on('TeleBot Settings', {
	fetch_now: function(frm){
		frappe.call({
			method: "telebot_integration.telebot_integration.doctype.telebot_settings.telebot_settings.create_telegram_chat",
			args: {bot_name: frm.doc.name},
			freeze: true
		})
	}
});
