# Copyright (c) 2024, Promantia Business Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from redminelib import Redmine


def get_redmine_instance():
    return Redmine('https://redmine.promantia.in', username='hari.madhavan@promantia.com', password='nopassword')

class RM_Project(Document):
	
	def db_insert(self, *args, **kwargs):
		pass

	def load_from_db(self):
		redmine=get_redmine_instance()
		project = redmine.project.get(self.name)
		data = {
			"name" : project.id,
			"project_name" : project.name,
			"identifier" : project.identifier,
			"description" : project.description
		}
		super(Document, self).__init__(data)

	def db_update(self):
		pass

	@staticmethod
	def get_list(args):
		#redmine = Redmine('https://redmine.promantia.in', username='hari.madhavan@promantia.com', password='nopassword')

		redmine=get_redmine_instance()
		projects = redmine.project.all().filter(status=1)
		return [frappe._dict({
			"name" : p.id,
			"project_name" : p.name,
			"identifier" : p.identifier,
			"description" : p.description
		}) for p in projects ]

	@staticmethod
	def get_count(args):
		redmine = Redmine('https://redmine.promantia.in', username='hari.madhavan@promantia.com', password='nopassword')
		#redmine=get_redmine_project()
		return len(redmine.project.all().filter(status=0))



	@staticmethod
	def get_stats(args):
		pass

