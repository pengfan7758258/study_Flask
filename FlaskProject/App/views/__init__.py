from App.views.first_blue import blue


def init_views(app):
    app.register_blueprint(blue)