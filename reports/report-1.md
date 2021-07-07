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
Params: total_count 100
Total time for 100 requests = 118 ms.
Avg time per request = 1.18 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 100, max_conn 100
Total time for 100 requests = 101 ms.
Avg time per request = 1.01 ms.

-----------------------------------------
```

Run http client module based client tests.
```sh
# python3 httpclient/httpclient-threading.py 

Sequential Requests:
Params: total_count 100
Total time for 100 requests = 102 ms.
Avg time per request = 1.02 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 100, threads_count 100
Total time for 100 requests = 137 ms.
Avg time per request = 1.37 ms.

-----------------------------------------
```

Run requests module based client tests.
```sh
# python requests/requests-threading.py 

Sequential Requests:
Params: total_count 100
Total time for 100 requests = 200 ms.
Avg time per request = 2.0 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 100, threads_count 100
Total time for 100 requests = 237 ms.
Avg time per request = 2.37 ms.

-----------------------------------------
```