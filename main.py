import random

# задання модулю m, за яким будуть вестись розрахунки.
m = int(input("\tВведіть значення m.\nm = "))

# розв’язання рівняння виду a mod m = x.
a = int(input("\n\tВведіть значення а.\na  = "))
print("a mod m = ", a % m)

# розв’язання рівняння виду a^b mod m = x.
b = int(input("\n\tВведіть значення b.\nb = "))
print("a^b mod m = ", (a ** b) % m)

# розв’язання рівняння виду a*x ≡ b mod m.
x = (b % m) / a
print("\nb mod m = a * x\nx = ", x, "\nb mod m = ", a * x)

# генерування простого числа у діапазоні від A до B.
print("\nВивід простих чисел від A до B")
a = int(input("A = "))
b = int(input("B = "))
n = b - a
mas = [0] * n
for i in range(n):
    mas[i] = i

mas[1] = 0

f = 2
while f < n:
    if mas[f] != 0:
        j = f * 2
        while j < n:
            mas[j] = 0
            j = j + f
    f += 1

primes = []
for i in mas:
    if mas[i] != 0:
        primes.append(mas[i])

del a
print("\nМасив простих чисел:\n", primes)
random_index = random.randrange(len(primes))
print("\nВипадкове просте число з масиву: ", primes[random_index])
