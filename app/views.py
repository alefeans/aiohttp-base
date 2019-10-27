from aiohttp import web


async def root(request):
    raise web.HTTPFound('/healthcheck')


async def healthcheck(request):
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Healthcheck
    produces:
    - application/json
    responses:
        "200":
            description: successful operation
        "405":
            description: invalid HTTP Method
    """
    return web.json_response({'message': "I'm fine and you ?"})
