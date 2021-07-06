Summary findings for PUT requests.
- Sequential requests is faster with aiohttp
- parallel requests is slower with aiohttp compared to other modules with threading.

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
Total time for 100 requests = 110 ms.
Avg time per request = 1.1 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 100, max_conn 100
Total time for 100 requests = 6502 ms.
Avg time per request = 65.02 ms.

-----------------------------------------
```

Run http client module based client tests.
```sh
# python3 httpclient/httpclient-threading.py 

Sequential Requests:
Params: total_count 100
Total time for 100 requests = 114 ms.
Avg time per request = 1.14 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 100, threads_count 100
Total time for 100 requests = 142 ms.
Avg time per request = 1.42 ms.

-----------------------------------------
```

Run requests module based client tests.
```sh
# python requests/requests-threading.py 

Sequential Requests:
Params: total_count 100
Total time for 100 requests = 205 ms.
Avg time per request = 2.05 ms.

-----------------------------------------

Parallel Requests:
Params: total_count 100, threads_count 100
Total time for 100 requests = 380 ms.
Avg time per request = 3.8 ms.

-----------------------------------------
```