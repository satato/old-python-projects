__author__ = 'Amber Melton'


for x in range(0,10):
    print("Amber")


for num in range(1, 101):
    if num != 100:
        print(num, end=" ")
    else:
        print(num)


for num in range(1, 101):
    if num % 2 == 0 and num != 100:
        print(num, end=" ")
    elif num == 100:
        print(num)


for num in range(1, 101):
    if num % 5 == 0 and num != 100:
        print(num, end=" ")
    elif num == 100:
        print(num)


i = 10
while i >= 0:
    print(i)
    i -= 1
print("Blastoff!")


name = "Amber"
for x in name:
    print(x)


for x in range(0, 100):
    print(x, end=", ")


x = 99
while x > 0:
    print(x, end=", ")
    x -= 1


if x == 0:
    print(x)


sum = 0
for x in range(0,100):
    sum = sum+x
print(sum)


factorial10 = 10
for x in range(1,10):
    factorial10 = factorial10*x

print(factorial10)




rangemin = input("Please Select a Minimum for your range:")
rangemax = input("Please input a maximum for your range:")
print("Thank you")

sum = 0
for x in range(int(rangemin), int(rangemax)+1):
    sum = sum+x
print("The sum of all of the integers within your selected range is: ", sum)


userinput = input("Please state a value for factorial:")
print("Thank you")

factorial = int(userinput)
for x in range(1,factorial):
    factorial = factorial * x
print("The factorial of your selected value, ", userinput,", is: ", factorial)


input("Press Enter to Continue...")


index = 0
population = 106.2
while population < 120:
    population = population*1.017
    index += 1
year = 2005 + index
print("The year in which the population of Mexico will reach 120 million is ", year)

input("Press Enter to Exit")