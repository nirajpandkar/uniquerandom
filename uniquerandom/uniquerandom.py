import random
count = 0
prev = 0


def int():
    randomnum = random.randint(1, 10)
    global count
    global prev
    if count == 0:
        prev = randomnum
        print(randomnum)
        count = 1
    else:
        if randomnum == prev:
            uniquerandom()
        else:
            print(randomnum)
            prev = randomnum

uniquerandom()




