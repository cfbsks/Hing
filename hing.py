#!/usr/bin/env python3

import argparse
import subprocess


def test_request(target_url, proxy=None, num_requests=10, user_agent=None):
    # Proxy configuration
    proxy_url = proxy if proxy else None

    # Execute curl and collect timing data
    times = []
    success_count = 0

    for i in range(num_requests):
        cmd = ['curl', '-o', '/dev/null', '-s', '-w', "%{http_code} %{time_total}", '-A', user_agent, target_url]
        if proxy_url:
            cmd.insert(1, '--proxy')
            cmd.insert(2, proxy_url)
        result = subprocess.run(cmd, capture_output=True, text=True)
        response_code, time = result.stdout.strip().split()

        # Convert time from seconds to milliseconds
        time_ms = float(time) * 1000  # convert to ms

        if response_code == "200":
            print(f"Request {i + 1}: {time_ms:.2f} ms")  # change "s" to "ms"
            times.append(time_ms)
            success_count += 1
        else:
            print(f"Request {i + 1} failed with HTTP code: {response_code}")

    if not times:
        print("\nAll requests failed.")
        return

    # Compute and print average, maximum, and minimum times
    average = sum(times) / len(times)
    max_time = max(times)
    min_time = min(times)
    success_rate = (success_count / num_requests) * 100

    print(f"\nAverage time: {average:.2f} ms")
    print(f"Maximum time: {max_time:.2f} ms")
    print(f"Minimum time: {min_time:.2f} ms")
    print(f"Success rate: {success_rate:.2f}%")


def main():
    parser = argparse.ArgumentParser(description='Test HTTP request times.')
    parser.add_argument('target_url', type=str, help='Target URL to test.')
    parser.add_argument('--num_requests', type=int, default=10, help='Number of requests to perform. Default is 10.')
    parser.add_argument('--proxy', type=str, default=None,
                        help='Proxy address to use. Format should be http://proxy-address:proxy-port')
    parser.add_argument('--user_agent', type=str,
                        default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                        help='User-Agent to be used for the requests. Default is a common browser user-agent.')

    args = parser.parse_args()

    test_request(args.target_url, args.proxy, args.num_requests, args.user_agent)


if __name__ == "__main__":
    main()
