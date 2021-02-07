from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_list_project = app.project.get_project_list()
    app.project.create()
    project = Project(name_project=str("test"), status="stable",
                      description="test", view_status="public")
    app.project.fill_form_project(project)
    app.project.confirm_add_project()
    new_list_project = app.project.get_project_list()
    assert len(old_list_project) == len(new_list_project)
    old_list_project.append(project)
