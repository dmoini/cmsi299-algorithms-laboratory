# 00499 - What's The Frequency, Kenneth?
import sys
from collections import defaultdict
import string

for line in sys.stdin:
    counts = defaultdict(int)
    for w in list(line.strip()):
        if w in string.ascii_letters:
            counts[w] += 1
    max_count = max(counts.values())
    letters = [l for l, c in counts.items() if c == max_count]
    print(''.join(sorted(letters)), max_count)