n = int(input('Enter a number: '))

print('Using for: ')
for i in range(n):
    print('*', end='')
print()

print('Using while: ')
c = n
while c > 0:
    print('*', end='')
    c -= 1
print()

print('Using the replication operator: ')
print('*' * n)
