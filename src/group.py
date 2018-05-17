import pykeepass
from pykeepass import PyKeePass

class Group:
    name = ""
    icon = ""
    notes = ""
    uuid = ""
    parent_group_name = ""
    group_path = ""
    parent_group_path = ""

    def __init__(self, name, group_path, uuid=uuid, icon=icon, notes=notes, parent_group_name=parent_group_name, parent_group_path=parent_group_path):
        self.name = name
        self.uuid = uuid
        self.icon = icon
        self.notes = notes
        self.group_path = group_path
        self.parent_group_path = parent_group_path

    def change_name(self, name):
        self.name = name

    def change_icon(self, icon):
        self.icon = icon

    def change_notes(self, notes):
        self.note = notes

    #def change_root_group(self, path):
        #todo

    def get_name(self):
        return self.name

    def get_icon(self):
        return self.icon

    def get_notes(self):
        return self.notes

    def get_uuid(self):
        return self.uuid

    def get_parent_group_name(self):
        return self.parent_group_name

    def get_group_path(self):
        return self.group_path

    def get_parent_group_path(self):
        return self.parent_group_path

    