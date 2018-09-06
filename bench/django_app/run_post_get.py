from bench_common import *


def bench_post_get():
    result = call(environ_post())
    assert result['ok']
    record_id = result['id']
    result = call(environ_get(record_id))
    assert result['project'] == 'treehook'


def run_bench(runner):
    migrate()
    runner.bench_func('bench_django_post_get', bench_post_get)


if __name__ == "__main__":
    run_bench(perf.Runner())
