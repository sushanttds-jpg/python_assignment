s1 = {1, 2, 3, 5, 6}
s2 = {6, 8, 5, 3}
s1.add(10) 
s1.discard(2) 
print(s1.union(s2)) 
print(s1.intersection(s2)) 
print(s1.difference(s2)) 
print(s1.isdisjoint(s2))
print(s1.issubset({1, 3, 5, 6, 8, 10})) 
print(s1.issuperset({3, 5}))
s1.remove(1)
s1.clear() 