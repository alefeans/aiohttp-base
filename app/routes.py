from .views import healthcheck, root


def setup_routes(app):
    app.router.add_get('/', root, name='root', allow_head=False)
    app.router.add_get('/healthcheck', healthcheck, name='healthcheck', allow_head=False)
