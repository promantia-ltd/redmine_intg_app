frappe.treeview_settings["RM_Project"] = {
    get_tree_nodes: "redmine_intg.rm_masters.doctype.rm_project.rm_project.get_children",
    get_tree_root: false,
    root_label: "RM Projects",
    filters: [

    ],
    fields: [
        { fieldtype: "Data", fieldname: "project_name", label: __("New Project Name"), reqd: true },
        {
            fieldtype: "Check",
            fieldname: "is_group",
            label: __("Is Group"),
            description: __("Child nodes can be only created under 'Group' type nodes"),
        },
    ],
    ignore_fields: ["parent_rm_project"],
};                              