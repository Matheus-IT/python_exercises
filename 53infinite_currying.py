def add(a=0):
    return lambda b=0: add(a + b) if b else a


print(add(3)(4)(2)())
