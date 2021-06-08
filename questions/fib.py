#list of numbers
#add two previous numbers (Fibonacci)
#sum even value terms

count1 = 0
count2 = 1
total = 0

while count2 <= 4000000:

    if count2 % 2 == 0:

        total += count2
    temp = count2
    count2 = count2 + count1
    count1 = temp

print(total)

