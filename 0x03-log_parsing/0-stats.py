#!/usr/bin/python3
import re
import sys
from collections import defaultdict

# Define the status codes we care about
STATUS_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]
# Create a regular expression to match the log line format
LOG_PATTERN = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

def print_stats(total_size, status_counts):
    """Print the statistics: total file size and status codes counts."""
    print(f"File size: {total_size}")
    for code in STATUS_CODES:
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def log_parsing():
    """Parse the log lines, compute statistics and print them."""
    total_size = 0
    status_counts = defaultdict(int)  # Default to 0 for missing status codes
    line_count = 0

    try:
        for line in sys.stdin:
            # Try to match the log line to the expected pattern
            match = LOG_PATTERN.match(line)
            if match:
                ip, date, status_code, file_size = match.groups()
                file_size = int(file_size)
                
                # Accumulate the total file size
                total_size += file_size
                # Update the count of the status code
                if status_code in status_counts:
                    status_counts[status_code] += 1

                # Increment the line count
                line_count += 1

                # Every 10 lines, print the stats
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (Ctrl + C)
        print_stats(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    log_parsing()


# Initialize metrics
total_file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

# Define regex pattern to match log lines
log_pattern = re.compile(
    r'^(?P<ip>(\d{1,3}\.){3}\d{1,3}) - \[(?P<date>.+?)\] "GET /projects/260 HTTP/1.1" '
    r'(?P<status_code>\d{3}) (?P<file_size>\d+)$'
)

def print_metrics():
    """Print the metrics collected so far."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

if __name__ == "__main__":
    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            match = log_pattern.match(line)
            if match:
                status_code = match.group('status_code')
                file_size = int(match.group('file_size'))
                
                # Update metrics
                total_file_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1

                # Print metrics every 10 lines
                if line_count % 10 == 0:
                    print_metrics()

    except KeyboardInterrupt:
        print_metrics()
