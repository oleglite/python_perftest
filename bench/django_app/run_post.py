from bench_common import *


def bench_post():
    call_fast(environ_post())


def run_bench(runner):
    migrate()
    runner.bench_func('bench_django_post', bench_post)


if __name__ == "__main__":
    run_bench(perf.Runner())
