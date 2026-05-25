# Copyright (c) 2026, lokesh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Attendance(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date
		employee: DF.Link
		in_time: DF.Time
		out_time: DF.Time
	# end: auto-generated types

	pass
