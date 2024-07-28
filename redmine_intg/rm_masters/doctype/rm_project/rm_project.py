# Copyright (c) 2024, Promantia Business Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from redminelib import Redmine


redmine=Redmine('https://redmine.promantia.in', username='hari.madhavan@promantia.com', password='nopassword')

def get_parent_projects() :
	
	projects = redmine.project.all().filter(status=1)
	parent_dict={}
	for p in projects:
		if hasattr( p , 'parent' ):
			parent_dict.update({ p.parent.id : p.parent.name})
	return parent_dict

class RM_Project(Document):
	
	def db_insert(self, *args, **kwargs):
		pass

	def load_from_db(self):
		parent_dict=get_parent_projects()		
		project = redmine.project.get(self.name)
		data = {
			"name" : project.id,
			"project_name" : project.name,
			"identifier" : project.identifier,
			"description" : project.description,
			"is_group" : ( 1 if project.id in parent_dict else 0),
			"parent_rm_project" : (project.parent.id if hasattr( project , 'parent' ) else None )
		
		}
		super(Document, self).__init__(data)

	def db_update(self):
		pass

	@staticmethod
	def get_list(args):
		#redmine = Redmine('https://redmine.promantia.in', username='hari.madhavan@promantia.com', password='nopassword')

		projects = redmine.project.all().filter(status=1)
		parent_dict=get_parent_projects()		
		project_dict=[frappe._dict({
			"name" : p.id,
			"project_name" : p.name,
			"is_group" : ( 1 if p.id in parent_dict else 0),
			"parent_rm_project" : (p.parent.id if hasattr( p , 'parent' ) else None ),
			"identifier" : p.identifier,
			"description" : p.description
		}) for p in projects]
		parent_dict={}
		return project_dict 

	@staticmethod
	def get_count(args):
		redmine = Redmine('https://redmine.promantia.in', username='hari.madhavan@promantia.com', password='nopassword')
		#redmine=get_redmine_project()
		return len(redmine.project.all().filter(status=1))

	@staticmethod
	def get_stats(args):
		pass

