def extend(val, lst=[]):
    lst.append(val)
    return lst

print(extend(1))
print(extend(2))
print(extend(3, []))
print(extend(4))
