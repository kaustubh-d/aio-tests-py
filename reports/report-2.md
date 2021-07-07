Report on run on code with git commit in current repo.

`commit: 7a2f6f654f6c72ded5720a250867fa3d786c837d`

Summary findings for PUT requests.

aiohttp performs better than other http modules when number of requests are scaled.

Run the aiohttp based server.
```sh
# python3 aiohttp/aiohttp-server.py 
======== Running on http://0.0.0.0:80 ========
(Press CTRL+C to quit)
API: PUT /hello
API: PUT /hello
...
```

Run the aiohttp based client tests.
```sh
# python3 aiohttp/aiohttp-client.py 

Sequential Requests:
Params: total_count 10000
Total time for 10000 requests = 10372 ms.
Avg time per request = 1.0372 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 10000, max_conn 1000
Total time for 10000 requests = 7525 ms.
Avg time per request = 0.7525 ms.

-----------------------------------------
```

Run http client module based client tests.
```sh
# python3 httpclient/httpclient-threading.py 

Sequential Requests:
Params: total_count 10000
Total time for 10000 requests = 10789 ms.
Avg time per request = 1.0789 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 10000, threads_count 10000
Total time for 10000 requests = 22078 ms.
Avg time per request = 2.2078 ms.

-----------------------------------------
```

Run requests module based client tests.
```sh
# python requests/requests-threading.py 

Sequential Requests:
Params: total_count 10000
Total time for 10000 requests = 20514 ms.
Avg time per request = 2.0514 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 10000, threads_count 10000
Total time for 10000 requests = 29091 ms.
Avg time per request = 2.9091 ms.

-----------------------------------------
```