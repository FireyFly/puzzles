import sys

def count(s):
  res = 0
  i = 0
  while i < len(s):
    if s[i] == '\\':
      if s[i+1] == 'x':
        i += 4
      else:
        i += 2
    else:
      i += 1
    res += 1
  return res - 2

def count2(s):
  res = 0
  i = 0
  while i < len(s):
    if s[i] == '"' or s[i] == '\\':
      res += 2
    else:
      res += 1
    i += 1
  return res + 2

#total = sum(len(line) - count(line) for line in sys.stdin)
total = sum(count2(line) - len(line) for line in sys.stdin)
print(total)
