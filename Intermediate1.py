import random
def randInt(min = 0,max = 100):
    if max<0:
        print('sorry we need a max number greater than 0')
    elif min > max:
        print('sorry please give a max greater than the min')
    else: 
        if max != 100 and min != 0:
            return round(random.random()*(max-min)+min)
        if min != 0:
            return round(random.random()*(100-min)+min)
        if max != 100:
            return round(random.random()*max)
    return round(random.random()*100)
print(f"should print a random integer between 0 to 100 randInt() = {randInt()}")
print(f"should print a random integer between 0 to 50 between 0 and 50 randInt(max = 50) = {randInt(max = 50)}")
print(f"should print a random integer between 0 to 50 between 50 and 100, randInt(min = 50) = {randInt(min = 50)}")
print(f"should print a random integer between 0 to 50 between 50 and 100 randInt(min = 22, max = 25) = {randInt(min = 22, max = 25)}")
print(f" the edge case of min>max, randInt(min = 7, max = 2) {randInt(min = 7, max = 2)}")
print(f" the edge case of 0<max, randInt(max = -5) {randInt(max = -5)}")

