from model.project import Project


def test_del_project(app, config):
    app.session.login("administrator", "root")
    app.project.open_project()
    if len(app.project.get_project_list()) == 0:
        app.project.create()
        app.project.fill_form_project(Project(name_project=str("test"), status="stable",
                                              description="test", view_status="public"))
        app.project.confirm_add_project()
    old_list_project = app.soap.get_project_list(username=config['web']["username"], password=config['web']["password"], baseUrl=config['web']['baseUrl'])
    app.project.del_project()
    app.project.open_project()
    new_list_project = app.soap.get_project_list(username=config['web']["username"], password=config['web']["password"], baseUrl=config['web']['baseUrl'])
    assert len(old_list_project) - 1 == len(new_list_project)
    old_list_project[0:1] = []
    assert old_list_project == new_list_project