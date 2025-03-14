import argparse
from . import utils
from . import suffix_tree

SUB = 0
CHILDREN = 1

def get_args():
    parser = argparse.ArgumentParser(description='Suffix Array')
    parser.add_argument('--reference', help='Reference sequence file', type=str)
    parser.add_argument('--string', help='Reference sequence', type=str)
    parser.add_argument('--query', help='Query sequences', nargs='+', type=str)
    return parser.parse_args()

def build_suffix_array(T):
    return sorted(range(len(T)), key=lambda i: T[i:])

def lcp(s, T_sub):
    count = 0
    for a, b in zip(s, T_sub):
        if a == b:
            count += 1
        else:
            break
    return count

def search_array(suffix_array, T, pattern):
    lo, hi = 0, len(suffix_array)
    best = 0
    while lo < hi:
        mid = (lo + hi) // 2
        suffix = T[suffix_array[mid]:]
        if suffix < pattern:
            lo = mid + 1
        else:
            hi = mid
    if lo < len(suffix_array):
        best = max(best, lcp(pattern, T[suffix_array[lo]:]))
    if lo - 1 >= 0:
        best = max(best, lcp(pattern, T[suffix_array[lo-1]:]))
    return best

def main():
    args = get_args()
    T = None
    if args.string:
        T = args.string
    elif args.reference:
        reference = utils.read_fasta(args.reference)
        T = reference[0][1]
    array = build_suffix_array(T)
    if args.query:
        for query in args.query:
            match_len = search_array(array, T, query)
            print(f'{query} : {match_len}')

if __name__ == '__main__':
    main()
