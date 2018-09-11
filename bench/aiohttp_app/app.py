import argparse
import asyncio
import logging.config
import uvloop
from aiohttp import web

from record import get_record


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


logging.config.dictConfig({'version': 1, 'disable_existing_loggers': True})


async def handle_ping(request):
    return web.Response(text='Hello')


async def handle_version(request):
    return web.Response(text='aiohttp_app')


async def handle_read(request):
    record_id = request.match_info.get('record_id')
    record = await get_record(record_id)
    return web.json_response(record)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    args = parser.parse_args()

    app = web.Application()
    app.add_routes([
        web.get('/record/read/{record_id}', handle_read),
        web.get('/version', handle_version),
        web.get('/', handle_ping),
    ])
    web.run_app(app, access_log=None, path=args.path)
