#find sum of squares of first 100 numbers
# #find sum of first 100 numbers
#square sum of first 100 numbers
total = 0
num = 1
while num <= 100:
    total += num * num
    num += 1

new_tot = 0
new_num = 1
while new_num <= 100:
    new_tot += new_num
    new_num += 1

sumsquared = new_tot * new_tot

diff = sumsquared - total

print(diff)