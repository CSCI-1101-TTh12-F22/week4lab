## Exercise 1
for i in range(3,15):
    print(i)

## Exercise 2
total = 0
for i in range(3, 16, 2):
    total += i
print(total)

## Exercise 3
for i in range(50,0,-5):
    print(i)

## Exercise 4
theword = input("provide a word: ")
for c in theword:
    print(c, end="*", sep="")
print()
    
## Exercise 5
a = input("int1: ")
b = input("int2: ")
c = input("int3: ")
print(a, b, c, sep="", end="?")
print(a + b + c + "?", end="")
    
# Exercise 6
print(f'{a}{b}{c}?', end="")

# Exercise 7
name = input("name: ")
age = int(input("age: "))
print(f'{name} {age/7:.2f}')

# Exercise 8
major = input("major: ")
year = input("year: ")
g = open("mytext.txt", "w")
g.write(f'{name}\n{age}\n{major}\n{year}\n')
g.close()

# Exercise 9
with open("mytext.txt") as f:
    for line in f:
        print(line.rstrip().upper())
