# test file (not actual experiment)
from src.suffix_trie import build_suffix_trie, search_trie
from src.suffix_array import build_suffix_array, search_array
from src.suffix_tree import search_tree

if __name__ == "__main__":
    # sample text / patterns for testing
    text = "banana"
    patterns = ["ana", "ban", "nana", "apple"]

    # test suffix trie
    trie = build_suffix_trie(text)
    print("Suffix Trie Results:")
    for pat in patterns:
        result = search_trie(trie, pat)
        print(f"Pattern '{pat}': prefix overlap length = {result}")

    # test suffix array
    sa = build_suffix_array(text)
    print("\nSuffix Array Results:")
    for pat in patterns:
        result = search_array(sa, text, pat)
        print(f"Pattern '{pat}': prefix overlap length = {result}")

    # test suffix tree
    tree = {
        "banana": {},
        "anana": {},
        "nana": {},
        "ana": {},
        "na": {},
        "a": {}
    }
    print("\nSuffix Tree Results (using a dummy tree):")
    for pat in patterns:
        result = search_tree(tree, pat)
        print(f"Pattern '{pat}': prefix overlap length = {result}")
