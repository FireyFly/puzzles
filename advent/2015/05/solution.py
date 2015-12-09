import re
import sys

#def ok(s):
#  return len(re.findall(r'[aeiou]', s)) >= 3 and \
#         re.search(r'(.)\1', s) and \
#         not re.search(r'ab|cd|pq|xy', s)

def ok(s):
  return re.search(r'(..).*\1', s) and \
         re.search(r'(.).\1', s)

count = sum(1 for line in sys.stdin if ok(line))
print(count)
