import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import argparse
from . import utils

def get_args():
    parser = argparse.ArgumentParser(description='Suffix Trie')

    parser.add_argument('--reference',
                        help='Reference sequence file',
                        type=str)

    parser.add_argument('--string',
                        help='Reference sequence',
                        type=str)

    parser.add_argument('--query',
                        help='Query sequences',
                        nargs='+',
                        type=str)

    return parser.parse_args()

def build_suffix_trie(text):
    trie = {}
    for i in range(len(text)):
        node = trie
        for c in text[i:]:
            if c not in node:
                node[c] = {}
            node = node[c]
    return trie

def search_trie(trie, pattern):
    node = trie
    count = 0
    for c in pattern:
        if c in node:
            count += 1
            node = node[c]
        else:
            break
    return count


def main():
    args = get_args()

    T = None

    if args.string:
        T = args.string
    elif args.reference:
        reference = utils.read_fasta(args.reference)
        T = reference[0][1]

    trie = build_suffix_trie(T)

    if args.query:
        for query in args.query:
            match_len = search_trie(trie, query)
            print(f'{query} : {match_len}')

if __name__ == '__main__':
    main()
