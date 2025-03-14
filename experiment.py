import time
import random
import matplotlib.pyplot as plt
from src.suffix_trie import build_suffix_trie, search_trie
from src.suffix_array import build_suffix_array, search_array
from src.suffix_tree import build_suffix_tree, search_tree

def generate_random_dna(n):
    return ''.join(random.choices("ACGT", k=n))

# Use smaller string sizes to reduce memory usage
string_sizes = [100, 200, 300, 400, 500]

build_times_trie = []
build_times_tree = []
build_times_array = []
search_times_trie = []
search_times_tree = []
search_times_array = []
pattern = "ACGTAC"

for n in string_sizes:
    T = generate_random_dna(n)
    
    # Build Suffix Trie (wrap in try/except in case of memory issues)
    try:
        start = time.perf_counter()
        trie = build_suffix_trie(T)
        end = time.perf_counter()
        build_times_trie.append(end - start)
    except MemoryError:
        build_times_trie.append(None)
        trie = None

    # Build Suffix Tree (wrap in try/except)
    try:
        start = time.perf_counter()
        tree = build_suffix_tree(T)
        end = time.perf_counter()
        build_times_tree.append(end - start)
    except MemoryError:
        build_times_tree.append(None)
        tree = None

    # Build Suffix Array (should be memory-efficient)
    start = time.perf_counter()
    array = build_suffix_array(T)
    end = time.perf_counter()
    build_times_array.append(end - start)
    
    # Search using Suffix Trie
    try:
        start = time.perf_counter()
        _ = search_trie(trie, pattern)
        end = time.perf_counter()
        search_times_trie.append(end - start)
    except Exception:
        search_times_trie.append(None)
    
    # Search using Suffix Tree
    try:
        start = time.perf_counter()
        _ = search_tree(tree, pattern)
        end = time.perf_counter()
        search_times_tree.append(end - start)
    except Exception:
        search_times_tree.append(None)
    
    # Search using Suffix Array
    start = time.perf_counter()
    _ = search_array(array, T, pattern)
    end = time.perf_counter()
    search_times_array.append(end - start)

def safe_list(vals):
    return [v if v is not None else 0 for v in vals]

plt.figure()
plt.plot(string_sizes, safe_list(build_times_trie), marker='o', label='Suffix Trie')
plt.plot(string_sizes, safe_list(build_times_tree), marker='o', label='Suffix Tree')
plt.plot(string_sizes, build_times_array, marker='o', label='Suffix Array')
plt.xlabel('String Size')
plt.ylabel('Build Time (seconds)')
plt.title('Build Time Comparison')
plt.legend()
plt.savefig("build_time_comparison.png")
plt.close()

plt.figure()
plt.plot(string_sizes, safe_list(search_times_trie), marker='o', label='Suffix Trie')
plt.plot(string_sizes, safe_list(search_times_tree), marker='o', label='Suffix Tree')
plt.plot(string_sizes, search_times_array, marker='o', label='Suffix Array')
plt.xlabel('String Size')
plt.ylabel('Search Time (seconds)')
plt.title('Search Time Comparison')
plt.legend()
plt.savefig("search_time_comparison.png")
plt.close()

print("Experiment completed. Figures saved as build_time_comparison.png and search_time_comparison.png")
