from bench_common import *


def bench_get():
    call_fast(environ_get(random_source.randint(MIN_ID, MAX_ID)))


def run_bench(runner):
    migrate()
    runner.bench_func('bench_django_get', bench_get)


if __name__ == "__main__":
    run_bench(perf.Runner())
