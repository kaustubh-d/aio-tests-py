#!/usr/bin/env python3

import requests
import threading
import time

def print_report(total_count, total_time_ms):
    print("Total time for {} requests = {} ms.".format(
        total_count, total_time_ms))
    print("Avg time per request = {} ms.\n".format(
        total_time_ms / total_count))
    print("-----------------------------------------\n")

def thread_func_put_api(session):
    resp = session.put("http://localhost/hello", data="Hello World!!")

    assert resp.status_code == 200
    return

# Test case 1: Runs each request in sequence.
def test_case_seq_reqs(total_count):
    print("\nSequential Requests:\nParams: total_count {}".format(total_count))
    client_session = requests.Session()

    start_time = time.perf_counter()
    for i in range(total_count):
        thread_func_put_api(client_session)
    end_time = time.perf_counter()

    total_time_ms = int(round((end_time - start_time) * 1000))

    print_report(total_count, total_time_ms)

# Test case 2: Runs all requests in parallel, 1 request per thread.
def test_case_parallel(total_count):
    print("\nParallel Requests:\nParams: total_count {}, threads_count {}".format(
        total_count, total_count))
    client_session = requests.Session()

    # Start threads to upload objects.
    request_threads = []
    start_time = time.perf_counter()
    for i in range(total_count):
        t = threading.Thread(
            target=thread_func_put_api, args=(client_session,))
        request_threads.append(t)
        t.start()

    # Wait for threads to complete.
    total_time_ms = 0
    for i in range(total_count):
        request_threads[i].join()

    end_time = time.perf_counter()

    total_time_ms = int(round((end_time - start_time) * 1000))
    print_report(total_count, total_time_ms)

def main():
    total_count = 100
    # Sequential requests.
    test_case_seq_reqs(total_count=total_count)

    # Parallel requests with threads - all
    test_case_parallel(total_count=total_count)


if __name__ == '__main__':
    main()