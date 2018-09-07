import logging
from aiohttp import web


logging.config.dictConfig({'disable_existing_loggers': True})

# TODO: http://docs.aiohttp.org/en/latest/deployment.html

async def handle_ping(request):
    return web.Response(text='Hello')


app = web.Application()
app.add_routes([
    web.get('/', handle_ping),
])
web.run_app(app, access_log=None)
