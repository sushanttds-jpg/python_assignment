from collections import namedtuple, deque, Counter, defaultdict, ChainMap
employee = namedtuple("employee", ["name", "age"])
emp = employee("Harendra", 34)
q = deque([52, 53])
q.appendleft(0)
# Counter [54]
c = Counter([27, 55, 56])
# defaultdict [57]
d = defaultdict(int)
d['a'] += 1
address = {"City": "Kathmandu"}
salary = {"monthly": 50000}
info = ChainMap(address, salary)