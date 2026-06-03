from collections import namedtuple, deque, Counter, defaultdict, ChainMap

employee = namedtuple("employee", ["name", "age"])
emp = employee("Sushant", 19)
print("NamedTuple:", emp)
q = deque([52, 53])
q.appendleft(0)
print("Deque:", q)
c = Counter([27, 55, 56])
print("Counter:", c)
d = defaultdict(int)
d['a'] += 1
print("DefaultDict:", d)
address = {"City": "Udayapur"}
salary = {"monthly": 450000}
info = ChainMap(address, salary)
print("ChainMap:", info)