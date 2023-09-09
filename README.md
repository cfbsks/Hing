# Hing - HTTP Latency Tester
Hing is a straightforward HTTP latency testing tool built on top of Python. It uses curl under the hood to measure the latency of HTTP requests, making it simple but effective for getting a quick idea of your server's performance.

## Feature
- Test latency against any HTTP/HTTPS target URL.
- Specify a proxy to route your requests through.
- Specify a custom user-agent string for the requests.
- View average, maximum, and minimum latencies from the results.
- Ability to specify the number of requests you'd like to perform.

## Getting Started

### Prerequisites
- Docker installed on your machine.

### Setup

1. Clone the repository:
    ```
    git clone https://github.com/cfbsks/Hing.git
    cd Hing
    ```

2. Build the Docker image:
    ```
    docker build -t hing .
    ```

### Usage

You can run Hing using the built Docker image. Here's an example:

`docker run hing [TARGET_URL] --num_requests [NUMBER_OF_REQUESTS] --proxy [PROXY_URL] --user_agent [CUSTOM_USER_AGENT]`  


```
usage: hing [-h] [--num_requests NUM_REQUESTS] [--proxy PROXY] [--user_agent USER_AGENT] target_url

Test HTTP request times.

positional arguments:
  target_url            Target URL to test.

options:
  -h, --help            show this help message and exit
  --num_requests NUM_REQUESTS
                        Number of requests to perform. Default is 10.
  --proxy PROXY         Proxy address to use. Format should be http://proxy-address:proxy-port
  --user_agent USER_AGENT
                        User-Agent to be used for the requests. Default is a common browser user-agent.

```

## Sample
```
> docker run --rm cfbsks/hing https://github.com/    
Request 1: 1551.11 ms
Request 2: 1125.48 ms
Request 3: 1102.52 ms
Request 4: 1151.87 ms
Request 5: 1371.84 ms
Request 6: 1205.24 ms
Request 7: 1123.81 ms
Request 8: 1199.39 ms
Request 9: 1365.89 ms
Request 10: 822.69 ms

Average time: 1201.98 ms
Maximum time: 1551.11 ms
Minimum time: 822.69 ms
Success rate: 100.00%

```