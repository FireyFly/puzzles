from queue import Queue
import re
import sys

def parse(s):
  expr, dst = s.split(" -> ")
  srcs = re.findall(r'[a-z0-9]+', expr)
  op = re.search(r'[A-Z]+', expr)
  op = 'ID' if op == None else op.group()
  return op, srcs, dst

parents = {}
children = {}
ops = {}
for line in sys.stdin:
  op, srcs, dst = parse(line.replace("\n", ""))
  ops[dst] = op
  parents[dst] = srcs
  for src in srcs:
    if src not in children:
      children[src] = []
    children[src].append(dst)

def compute(op, v):
  if   op == 'ID':     return v[0]
  elif op == 'NOT':    return (2**16 - 1) ^ v[0]
  elif op == 'AND':    return v[0] & v[1]
  elif op == 'OR':     return v[0] | v[1]
  elif op == 'LSHIFT': return v[0] << v[1]
  elif op == 'RSHIFT': return v[0] >> v[1]
  else: raise("error: bad op '" + op + "'")

# Emulate circuit
def emulate(parents, children, ops, values = {}):
  values = dict(values)
  queue = Queue()

  def put(reg, value):
    values[reg] = value
    if reg not in children: return
    for r in children[reg]:
      if r not in values and all(x in values for x in parents[r]):
        queue.put(r)

  for k in children.keys():
    if re.search(r'^\d+$', k):
      put(k, int(k))

  while not queue.empty():
    reg = queue.get()
    op, srcs = ops[reg], parents[reg]
    srcs_ = [values[x] if x in values else int(x) for x in srcs]
    put(reg, compute(op, srcs_))

  return values


values = emulate(parents, children, ops)
print("a = {}".format(values['a']))

values = emulate(parents, children, ops, {'b': values['a']})
print("a = {}".format(values['a']))
