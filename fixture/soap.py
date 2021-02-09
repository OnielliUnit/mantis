from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password, baseUrl):
        client = Client(baseUrl + '/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password, baseUrl):
        client = Client(baseUrl + '/api/soap/mantisconnect.php?wsdl')

        try:
            soap_projects = client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return None
        projects = [Project(id=x.id, name_project=x.name, description=x.description) for x in soap_projects]
        return projects