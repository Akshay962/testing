from aiohttp import web
from plugins.akshay.extra import MNTFN
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Mᴋɴ Bᴏᴛᴢ")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

class akshay(object):
mntf = MNTFN
