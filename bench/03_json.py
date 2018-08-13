
"""Script for testing the performance of json parsing and serialization.
This will dump/load several real world-representative objects a few
thousand times. The methodology below was chosen for was chosen to be similar
to real-world scenarios which operate on single objects at a time.
"""

from __future__ import division

# Python imports
import json
import random
import perf

# Local imports
import six
if six.PY3:
    long = int


DICT = {
    'ads_flags': 0,
    'age': 18,
    'bulletin_count': 0,
    'comment_count': 0,
    'country': 'BR',
    'encrypted_id': 'G9urXXAJwjE',
    'favorite_count': 9,
    'first_name': '',
    'flags': 412317970704,
    'friend_count': 0,
    'gender': 'm',
    'gender_for_display': 'Male',
    'id': 302935349,
    'is_custom_profile_icon': 0,
    'last_name': '',
    'locale_preference': 'pt_BR',
    'member': 0,
    'tags': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'profile_foo_id': 827119638,
    'secure_encrypted_id': 'Z_xxx2dYx3t4YAdnmfgyKw',
    'session_number': 2,
    'signup_id': '201-19225-223',
    'status': 'A',
    'theme': 1,
    'time_created': 1225237014,
    'time_updated': 1233134493,
    'unread_message_count': 0,
    'user_group': '0',
    'username': 'collinwinter',
    'play_count': 9,
    'view_count': 7,
    'zip': ''
}


def make_dict(random):
    d = dict(DICT)
    d['session_number'] = random.randint(0, 2**64-1)
    return d

random_source = random.Random(5)  # Fixed seed.
DICT_GROUP = [make_dict(random_source) for _ in range(20)]


def bench_json_loads(objs):
    for obj in objs:
        res = json.loads(obj)
        res['theme'] = res['session_number'] + 1
        json.dumps(res)


if __name__ == "__main__":
    runner = perf.Runner()
    runner.metadata['description'] = "Benchmark json.loads()"

    objs = [json.dumps(d) for d in DICT_GROUP]

    runner.bench_func('json_loads', bench_json_loads, objs)
