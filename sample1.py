count = 0
for i in range(1, 101): 
    if i % 3 == 0:
        print(i)
        count += 1

print(f'Total number {count}')
