import argparse
import logging.config
from aiohttp import web
import aiosqlite


DB_PATH = '/home/db.sqlite3'


logging.config.dictConfig({'version': 1, 'disable_existing_loggers': True})


FIELDS = (
    'summary',
    'description',
    'project',
    'region',
    'total_budget',
    'info',
    'purpose',
    'department',
    'business',
    'is_budget',
    'customer',
    'owner',
    'approved_by',
    'created_at',
    'updated_at',
    'expires_at',
    'closed',
)


async def handle_ping(request):
    return web.Response(text='Hello')


async def get_record(record_id):
    sql = 'SELECT %s FROM mysite_record WHERE id=%s' % (
        ','.join(FIELDS), record_id
    )
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(sql) as cursor:
            async for row in cursor:
                return dict(zip(FIELDS, row))


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
        web.get('/', handle_ping),
        web.get('/record/read/{record_id}', handle_read)
    ])
    web.run_app(app, access_log=None, path=args.path)
