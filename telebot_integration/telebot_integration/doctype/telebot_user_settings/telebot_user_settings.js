// Copyright (c) 2023, Ahmed Al-farran and contributors
// For license information, please see license.txt

frappe.ui.form.on('TeleBot User Settings', {
	setup: function(frm) {
		frm.set_query("party", function() {
			var doctypes = ["User","Employee","Customer", "Supplier", "Contact"];
			return {
				filters: { "name": ["in", doctypes] }
			};
		});
	},

	
	party: function(frm){
		console.log("frm.doc.party = ", frm.doc.party);
		frm.set_value("telegram_user", undefined);
		frm.trigger("telegram_user");
	},	


	telegram_user: function(frm){
		let party_name = undefined;
		if(frm.doc.telegram_user){
			if(frm.doc.party){
				if(frm.doc.party == "User"){
					frappe.db.get_value(frm.doc.party, frm.doc.telegram_user, "full_name", (values) => {
						frm.set_value("telegram_user_name", values.full_name);
					});
				}
				else{
					frappe.db.get_value(frm.doc.party, frm.doc.telegram_user, "name", (values) => {
						frm.set_value("telegram_user_name", values.name);
					});
				}
			}
		}else{
			frm.set_value("telegram_user_name", undefined);
		}
	},


	generate_telegram_token: function(frm) {
		frappe.call({
			method: 'telebot_integration.telebot_integration.doctype.telebot_user_settings.telebot_user_settings.generate_telegram_token',
			args: {"is_group_chat":cur_frm.doc.is_group_chat},
			callback: (r) => {
				// console.log(r.message[0]);
				var telegram_token = r.message;

				cur_frm.set_value("telegram_token", telegram_token);
				frappe.model.get_value('TeleBot Settings', {name:frm.doc.telegram_settings}, 'bot_name', (r) => {
					if (r.bot_name) {
						if (window.isSecureContext && navigator.clipboard) {
							navigator.clipboard.writeText(frm.doc.telegram_token).then(()=> {
								frappe.show_alert({message:__('Telegram Token copied to your clipboard!'), indicator:'green'}, 20);
								window.open(`https://t.me/${r.bot_name}`, '_blank');
							});
						}else{
							frm.events.unsecuredCopyToClipboard(frm.doc.telegram_token, r.bot_name);
						}
					}
					
				});
				
			}
		});
	},


	unsecuredCopyToClipboard: (text, bot_name) => {
		const textArea = document.createElement("textarea");
		textArea.value = text;
		document.body.appendChild(textArea);
		textArea.focus();
		textArea.select();
		try {
		  document.execCommand('copy');
		} catch (err) {
		  console.error('Unable to copy to clipboard', err);
		}
		document.body.removeChild(textArea);
		frappe.show_alert({message:__('Telegram Token copied to your clipboard!'), indicator:'green'}, 20);
		window.open(`https://t.me/${bot_name}`, '_blank');
	  },
	

	get_chat_id : function(frm) {
		frappe.call({
			method: 'telebot_integration.telebot_integration.doctype.telebot_user_settings.telebot_user_settings.get_chat_id_button',
			args: {"telegram_token":cur_frm.doc.telegram_token, "telegram_settings":cur_frm.doc.telegram_settings},
			callback: (r) => {
				if (r.message && r.message != frm.doc.telegram_chat_id){
					cur_frm.set_value("telegram_chat_id", r.message);
					refresh_field("telegram_chat_id");
					frm.save();
				}
			}
		});
	}
});
