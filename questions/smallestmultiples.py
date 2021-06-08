# divide all numbers by 1 through to 20
# iterate through until


found = False
int = 200000000
while found == False:
    c = 0
    for x in range(1,21):
        if int % x == 0:
            c += 1
    if c == 20:
        print(int)
        found = True
    int += 1

