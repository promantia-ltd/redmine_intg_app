# Copyright (c) 2024, Promantia Business Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from redminelib import Redmine


class RM_Issue(Document):
	
	def db_insert(self, *args, **kwargs):
		pass

	def load_from_db(self):
		pass

	def db_update(self):
		pass

	@staticmethod
	def get_list(args):
		pass
	@staticmethod
	def load_children (args):
		issue_dict=[] 
		spent_hours=0
		for issue in args :
			spent_hours = 0
			for te in issue.time_entries :
				spent_hours=spent_hours+te.hours
			issue_dict.append({
				"redmine_id" : issue.id,
				"issue_type" : issue.tracker.name,
				"status" : issue.status.name,
				"issue_title" : issue.subject,
				"start_date" :issue.start_date,
				"description" :issue.description,
				"project" : issue.project.id,
				"due_date" : issue.due_date,
				"done_ratio" : issue.done_ratio,
				"estimated_hours": issue.estimated_hours,
				"spent_hours": spent_hours

			})   
		return issue_dict 


	@staticmethod
	def get_count(args):
		return 1

	@staticmethod
	def get_stats(args):
		pass

