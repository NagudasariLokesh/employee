# Copyright (c) 2026, lokesh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EmployeeDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		designation: DF.Data | None
		employee_name: DF.Data | None
		mobile: DF.Data | None
		role: DF.Literal["Admin", "HR", "Embedded Software", "Developer", "Tester", "Sales"]
		status: DF.Literal["Active", "Inactive"]
	# end: auto-generated types

	pass
