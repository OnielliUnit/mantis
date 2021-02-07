from model.project import Project


def test_del_project(app):

    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.open_project()
    if len(app.project.get_project_list()) == 0:
        app.project.create()
        app.project.fill_form_project(Project(name_project=str("test"), status="stable",
                                              description="test", view_status="public"))
        app.project.confirm_add_project()
    old_list_project = app.project.get_project_list()
    app.project.del_project()
    app.project.open_project()
    new_list_project = app.project.get_project_list()
    assert len(old_list_project) - 1 == len(new_list_project)
    old_list_project[0:1] = []
    assert old_list_project == new_list_project