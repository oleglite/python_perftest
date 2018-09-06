from bench_common import *


def bench_ping():
    call_fast(environ_ping())


def run_bench(runner):
    runner.bench_func('bench_django_ping', bench_ping)


if __name__ == "__main__":
    run_bench(perf.Runner())
