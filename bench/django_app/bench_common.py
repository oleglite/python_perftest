"""Test the performance of the Django template system.
This will have Django generate a 150x150-cell HTML table.
"""

import perf
import os
import sys
import json
import random
from io import BytesIO

import django.conf
from mysite.wsgi import application


random_source = random.Random(5)  # Fixed seed.

MIN_ID = 1
MAX_ID = 100000

DATA = {
    'summary': 'postponed evaluation of type annotations',
    'description': 'In addition, Django applies the following rule: if you set editable=False on the model field, any form created from the model via ModelForm will not include that field.',
    'project': 'treehook',
    'region': 'europe',
    'total_budget': 650012.5,
    'info': 'To avoid this failure, you must instantiate your',
    'purpose': 'Overriding the default fields',
    'department': 'Salary',
    'business': 'TYYJJB',
    'is_budget': True,
    'customer': 'jtmoore',
    'owner': 'hqsalmon',
    'approved_by': 'tewagner',
}
DATA_JSON = json.dumps(DATA)


def get_wsgi_environ(method='get', path='/', data=''):
    data = data.encode('utf-8')
    environ = dict(os.environ.items())
    environ['REQUEST_METHOD'] = method
    environ['PATH_INFO'] = path
    environ['CONTENT_LENGTH'] = len(data)
    environ['SERVER_NAME'] = 'localhost'
    environ['SERVER_PORT'] = 8000
    environ['wsgi.input'] = BytesIO(data)
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.run_once'] = True
    environ['wsgi.url_scheme'] = 'http'
    return environ


def environ_post():
    return get_wsgi_environ(
        'post',
        '/record/create',
        DATA_JSON
    )


def environ_get(record_id):
    return get_wsgi_environ(
        'get',
        '/record/read/%d' % record_id,
    )


def environ_ping():
    return get_wsgi_environ(
        'get',
        '/'
    )


def start_response(status, response_headers, exc_info=None):
    if not status.startswith('20'):
        print(status)
        print(exc_info)
        assert False


def call(environ):
    result = application(environ, start_response)
    try:
        return json.loads(''.join([b.decode() for b in result]))
    finally:
        if hasattr(result, 'close'):
            result.close()


def call_fast(environ):
    application(environ, start_response)


def migrate():
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate', '-v', '0'])

    from fill_in_records import fill_in_records
    fill_in_records()

