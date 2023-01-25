from . import __version__ as app_version

app_name = "telebot_integration"
app_title = "TeleBot Integration"
app_publisher = "Ahmed Al-farran"
app_description = "Telegram Bot Integration For FRAPPE & ERPNext"
app_email = "afarran1992@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/telebot_integration/css/telebot_integration.css"
app_include_js = "/assets/telebot_integration/js/telebot_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/telebot_integration/css/telebot_integration.css"
# web_include_js = "/assets/telebot_integration/js/telebot_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "telebot_integration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "telebot_integration.utils.jinja_methods",
#	"filters": "telebot_integration.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "telebot_integration.install.before_install"
# after_install = "telebot_integration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "telebot_integration.uninstall.before_uninstall"
# after_uninstall = "telebot_integration.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "telebot_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

doc_events = {

     "*": {
        #   "validate":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "onload":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "before_insert":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "after_insert":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "before_naming":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "before_change":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "before_update_after_submit":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "before_validate":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "before_save":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
        #   "autoname":[
        #        # "telegram_integration.telegram_integration.doctype.telegram_notification.telegram_notification.run_telegram_notifications",
        #        # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
        #        ],
          "after_insert":[
               "telebot_integration.telebot_integration.doctype.telebot_notification.telebot_notification.run_telegram_notifications",
               # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
               ],
          "on_update":[
               "telebot_integration.telebot_integration.doctype.telebot_notification.telebot_notification.run_telegram_notifications",
               # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
               ],
          "on_cancel":[
               "telebot_integration.telebot_integration.doctype.telebot_notification.telebot_notification.run_telegram_notifications",
               # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
               ],
          "on_submit":[
               "telebot_integration.telebot_integration.doctype.telebot_notification.telebot_notification.run_telegram_notifications",
               # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
               ],
          "on_change":[
               "telebot_integration.telebot_integration.doctype.telebot_notification.telebot_notification.run_telegram_notifications",
               # "telegram_integration.telegram_integration.doctype.sms_notification.sms_notification.run_sms_notifications"
               ],
	},
}


# Scheduled Tasks
# ---------------

scheduler_events = {
# 	"all": [
# 		"telegram_integration.tasks.all"
# 	],
	"daily": [
        "telebot_integration.telebot_integration.doctype.telebot_notification.telebot_notification.trigger_daily_alerts",
        "telebot_integration.telebot_integration.doctype.date_notification.date_notification.trigger_daily_alerts",
    ],
	# "hourly": [
	# 	"telegram_integration.telegram_integration.doctype.date_notification.date_notification.trigger_daily_alerts",
	# ],
# 	"weekly": [
# 		"telegram_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"telegram_integration.tasks.monthly"
# 	]
}


# Testing
# -------

# before_tests = "telebot_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "telebot_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "telebot_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"telebot_integration.auth.validate"
# ]
