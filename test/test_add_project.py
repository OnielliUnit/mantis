from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_list_project = app.soap.get_project_list(username="administrator", password="root")
    project = Project(name_project=str("test"), status="stable",
                      description="test", view_status="public")
    app.project.create()
    app.project.fill_form_project(project)
    app.project.confirm_add_project()
    new_list_project = app.soap.get_project_list(username="administrator", password="root")
    old_list_project.append(project)
    assert len(old_list_project) == len(new_list_project)

