# 00494 - Kindergarten Counting Game
import sys
import re

for line in sys.stdin.readlines():
    line = line.strip()
    word_count = count = len(re.findall("[a-zA-Z_]+", line))
    print(word_count)
