import sys

opening_quotation = True
for line in sys.stdin.readlines():
    line = line.strip()
    ans = ''
    for c in line:
        if c == '"':
            quote = '``' if opening_quotation else '\'\''
            ans += quote
            opening_quotation = not opening_quotation
        else:
            ans += c
    print(ans)