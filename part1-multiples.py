def doubleSum(number, max):
    sum = 0
    counter = number
    while counter < max:
        sum += counter 
        counter = counter + number
    return sum

max = 1000
sum = doubleSum(3, max) + doubleSum(5, max)
print(sum)