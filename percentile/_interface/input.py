import sys


def fetch_symbol() -> str:
    if 1 < len(sys.argv):
        return sys.argv[1]

    return input('Please provide a symbol to analyse:\n')


def is_numeric_output() -> bool:
    return 2 < len(sys.argv) and "--numeric" in sys.argv[2]
