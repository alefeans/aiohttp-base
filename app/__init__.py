import aiohttp_cors
from aiohttp import web
from aiohttp_swagger import setup_swagger
from .routes import setup_routes


def create_app():
    app = web.Application()
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*",)
    })
    setup_routes(app)
    for route in list(app.router.routes()):
        cors.add(route)

    setup_swagger(app=app,
                  description='An extensible Aiohttp Restful API template',
                  title='Aiohttp API',
                  api_version='v1',
                  swagger_url='api/v1/docs')
    return app
