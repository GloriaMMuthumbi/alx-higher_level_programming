#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def compute_metircs(lines):
    """
    Computes metrics based on the input

    Args:
        lines (list): list of lines of input

    Returns:
        dict: dictionary of metrics containing file size and status code
    """
    total_size = 0
    status_counts = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
    }

    for line in lines:
        parts = line.split()
        if len(parts) >= 8:
            status_code = int(parts[7])
            file_size = int(parts[8])
            total_size += file_size
            status_counts[status_code] += 1

    return {'total_size': total_size, 'status_counts': status_counts}


def print_statistics(metrics):
    """
    print staatistics based on computed metrics

    Args:
        metrics (dict): the metrics dictionary
    """
    print(f"Total file size: File size: {metrics['total_size']}")
    for status_code in sorted(metrics['status_counts']):
        count = metrics['status_counts'][status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def main():
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())

            if len(lines) % 10 == 0:
                metrics = compute_metrics(lines)
                print_statistics(metrics)
                lines = []

    except KeyboardInterrupt:
        metrics = comput_metrics(lines)
        print_statistics(metrics)

if __name__ == "__main__":
    main()
