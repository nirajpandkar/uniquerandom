import random
count = 0
prev = 0


def integer(minimum, maximum):
    randomnum = random.randint(minimum, maximum)
    global count
    global prev
    if count == 0:
        prev = randomnum
        count += 1
        return randomnum
    else:
        if randomnum == prev:
            integer(minimum, maximum)
        else:
            prev = randomnum
            return randomnum




