while True:
    n = int(input('Введите число от 3 до 20: '))
    if n < 3 or n > 20:
        continue
    else:
        break
list_a = []
list_b = []
for a in range(1, 21):
    for b in range(a + 1, 21):  
        if n % (a + b) == 0:  
            list_a.append(a)
            list_b.append(b)
for a, b in zip(list_a, list_b):
	break
result = ''.join(f"{a}{b}" for a, b in zip(list_a, list_b))
print(f" {n}-{result}")