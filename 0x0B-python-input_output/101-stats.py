#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def print_statistics(file_size, status_codes):
    """
    print all metrics

    Args:
        file_size (int): accumulated file size
        status codes (dict): dictionary of status codes
    """
    print("File size: {}".format(file_size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


def main():
    file_size = 0
    status_codes = {}
    count = 0
    valid = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if count == 10:
                print_statistics(file_size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass
        print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        raise


if __name__ == "__main__":
    main()
