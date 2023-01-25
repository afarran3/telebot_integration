# Copyright (c) 2023, Ahmed Al-farran and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import telegram
from frappe.model.document import Document
from frappe.utils import get_url_to_form
from frappe.utils.data import quoted
from frappe import _
from bs4 import BeautifulSoup
import asyncio

class TeleBotSettings(Document):
	pass


@frappe.whitelist()
def send_to_telegram(telegram_user, message, reference_doctype=None, reference_name=None, attachment=None):

	space = "\n" * 2
	telegram_chat_id = frappe.db.get_value('TeleBot User Settings', telegram_user,'telegram_chat_id')
	telegram_settings = frappe.db.get_value('TeleBot User Settings', telegram_user,'telegram_settings')
	telegram_token = frappe.db.get_value('TeleBot Settings', telegram_settings,'telegram_token')
	bot = telegram.Bot(token=telegram_token)


	if reference_doctype and reference_name:
		doc_url = get_url_to_form(reference_doctype, reference_name)
		telegram_doc_link = _("See the document at {0}").format(doc_url)
		if message:
			soup = BeautifulSoup(message, features="lxml")
			message = soup.get_text('\n') + space + str(telegram_doc_link)
			if type(attachment) is str:
				attachment = int(attachment)
			else:
				if attachment:
					attachment = 1
			if attachment == 1:
				attachment_url =get_url_for_telegram(reference_doctype, reference_name)
				message = message + space +  attachment_url
			asyncio.run(bot.send_message(chat_id=telegram_chat_id, text=message))
		
	else:
		message = space + str(message) + space
		asyncio.run(bot.send_message(chat_id=telegram_chat_id, text=message))



def get_url_for_telegram(doctype, name):
	doc = frappe.get_doc(doctype, name)
	return "{url}/api/method/telebot_integration.get_pdf.pdf?doctype={doctype}&name={name}&key={key}".format(
		url=frappe.utils.get_url(),
		doctype=quoted(doctype),
		name=quoted(name),
		key=doc.get_signature()
	)


@frappe.whitelist()
def create_telegram_chat(bot_name = None):
	# Called every 15 minutes via hooks
	bot_doc_list = []
	if bot_name:
		bot_doc_list.append(frappe.get_doc('TeleBot Settings', bot_name))
	else:
		bots = frappe.db.get_all('TeleBot Settings',['name'])

		for bot in bots:
			bot_doc_list.append(frappe.get_doc('TeleBot Settings', bot['name']))

	updates = get_updates(bot_doc_list)

	if updates:
		if bot_name:
			if bot_name in updates:
				frappe.msgprint(_("Telegram User Created"))
			else:
				frappe.msgprint(_('No Chats in {0}.').format(bot_name))

		for k, v in updates.items():
			for chat in v['chats']:
				existing_tele_chat = frappe.db.get_value("TeleBot User Settings", {'telegram_chat_id':chat['id'],'telegram_settings':k})
				if not existing_tele_chat:
					tele_chat = frappe.get_doc
					(
						{
							'doctype': 'TeleBot User Settings',
							'telegram_chat_id': chat['id'],
							'telegram_settings': k,
							'bot_name': v['bot_name']
						}
					)
					assign_values_based_on_type(tele_chat, chat)
				else:
					doc = frappe.get_doc('TeleBot User Settings',{'telegram_chat_id':chat['id'],'telegram_settings':k})
					assign_values_based_on_type(doc, chat)


def assign_values_based_on_type(tele_chat, chat):
	if chat['type'] == 'private':
		tele_chat.telegram_user_name = str(chat['first_name'] + " " + chat['last_name'])
	elif chat['type'] == 'supergroup' or 'channel':
		tele_chat.telegram_user_name = str(chat['title'])
	elif chat['type'] == 'group':
		tele_chat.telegram_user_name = str(chat['title'])
	tele_chat.save()


def get_updates(bot_doc_list):
	update_list = {}
	for bot_doc in bot_doc_list:
		try:
			chats = []
			bot = telegram.Bot(token = bot_doc.telegram_token)
			updates = asyncio.run(bot.get_updates(limit=100, offset=bot_doc.last_update_id))
			for update in updates:
				if update['message']:
					chats.append(update['message']['chat'])

				if update['channel_post']:
					chats.append(update['channel_post']['chat'])
				
				bot_doc.last_update_id = update['update_id']
			bot_doc.save()
			if chats:
				update_list[bot_doc.name] = { "bot_name" : bot_doc.bot_name, "chats": chats}

		except Exception as e:
			frappe.log_error(frappe.get_traceback(), f'{bot_doc.name} get updates error')
			# frappe.throw(_('An error occured. Check error log for more info'))
			continue

	return update_list