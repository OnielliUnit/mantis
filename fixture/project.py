from selenium.webdriver.support.select import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self):
        wd = self.app.wd
        self.open_project()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def open_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_form_project(self, project):
        wd = self.app.wd
        self.change_field_value(field_name='name', text=project.name_project)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_css_selector("input[name='inherit_global']").click()
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_status)
        self.change_field_value(field_name='description', text=project.description)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def confirm_add_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project()
            project_cache = []
            table = wd.find_element_by_xpath("//table[3]/tbody")
            rows = table.find_elements_by_tag_name("tr")
            for row in rows[2:]:
                cells = row.find_elements_by_tag_name("td")
                name_project = cells[0].text
                status = cells[1].text
                view_status = cells[3].text
                description = cells[4].text
                project_cache.append(Project(name_project=name_project, status=status,
                                             view_status=view_status, description=description))
        return list(project_cache)

    def del_project(self):
        wd = self.app.wd
        self.open_project()
        wd.find_element_by_xpath("//table[3]/tbody/tr[3]/td/a").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
