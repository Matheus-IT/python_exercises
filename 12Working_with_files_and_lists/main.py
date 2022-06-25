LENGTH = 5
nums1: list = []

db = open('.\\12Working_with_files_and_lists\\numbers.txt', 'w+')

print(f' - Type a sequence of {LENGTH} numbers')
for i in range(LENGTH):
	nums1.append(int(input(f' Number {i+1}: ')))
	db.write(f'{nums1[i]}\n')

db.seek(0)

nums2: list = []
for line in db:
	nums2.append(int(line))

print(f'VectA = {nums1}')
print(f'VectB = {nums2}')

db.close()
