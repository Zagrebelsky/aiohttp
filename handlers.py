from aiohttp import web
from service import handle


def setup_routes(app):
    app = web.Application()

    #app.router.add_post('/user', new_user)
