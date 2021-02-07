from sys import maxsize


class Project:

    def __init__(self, id=None, name_project=None, status=None, global_categories=None, view_status=None, description=None):
        self.id = id
        self.name_project = name_project
        self.status = status
        self.global_categories = global_categories
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.name_project, self.status, self.view_status, self.description)

    def __eq__(self, other):
        return (self.name_project is None or other.name_project is None or self.name_project == other.name_project) and self.status == other.status and self.view_status == other.view_status and self.description == other.description

    def id_or_max(self):
        if self.name_project:
            return str(self.name_project)
        else:
            return maxsize