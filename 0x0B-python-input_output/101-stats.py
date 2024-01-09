#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


import sys
from collections import defaultdict


def process_line(line, metrics):
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        metrics['total_size'] += file_size
        metrics['status_codes'][status_code] += 1
    except (ValueError, IndexError):
        pass

def print_statistics(metrics):
        """
            Print statistics.
        """
        for status_code in sorted(metrics['status_codes']):
            count = metrics['status_codes'][status_code]
            print(f"{status_code}: {count}")
