import aiosqlite


DB_PATH = '/home/db.sqlite3'

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


async def get_record(record_id):
    sql = 'SELECT %s FROM mysite_record WHERE id=%s' % (
        ','.join(FIELDS), record_id
    )
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(sql) as cursor:
            async for row in cursor:
                return dict(zip(FIELDS, row))
