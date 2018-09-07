import os

from bench_common import DATA, MAX_ID


def fill_in_records():
    print('IN_MEMORY_DB', bool(os.environ.get('IN_MEMORY_DB')))

    from mysite.models import Record
    amount = MAX_ID
    bulk_size = 1000
    for _ in range(0, amount, bulk_size):
        Record.objects.bulk_create(
            Record(**DATA)
            for _ in range(bulk_size)
        )

    assert Record.objects.count() == amount


if __name__ == '__main__':
    fill_in_records()
