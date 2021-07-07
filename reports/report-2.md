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
Params: total_count 1000
Total time for 1000 requests = 1040 ms.
Avg time per request = 1.04 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 1000, max_conn 100
Total time for 1000 requests = 727 ms.
Avg time per request = 0.727 ms.

-----------------------------------------
```

Run http client module based client tests.
```sh
# python3 httpclient/httpclient-threading.py 

Sequential Requests:
Params: total_count 1000
Total time for 1000 requests = 1441 ms.
Avg time per request = 1.441 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 1000, threads_count 1000
Total time for 1000 requests = 1877 ms.
Avg time per request = 1.877 ms.

-----------------------------------------
```

Run requests module based client tests.
```sh
# python requests/requests-threading.py 

Sequential Requests:
Params: total_count 1000
Total time for 1000 requests = 2738 ms.
Avg time per request = 2.738 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 1000, threads_count 1000
Total time for 1000 requests = 4369 ms.
Avg time per request = 4.369 ms.

-----------------------------------------
```