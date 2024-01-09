#!/usr/bin/python3
'''Module: 101-stats.py'''

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            ip, date, request, status_code, file_size = line.split(" ", 4)
            file_size = int(file_size)
            total_size += file_size
            status_codes[int(status_code)] += 1
            line_count += 1

            if line_count % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_codes):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")
        except ValueError:
            pass

except KeyboardInterrupt:
    print("File size:", total_size)
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
