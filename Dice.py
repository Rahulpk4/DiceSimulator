import random

minimum = 1
maximum = 6
count = 0
option = "yes"

while option == "yes":

    _side = random.randint(minimum, maximum)

    print(_side)

    count = count + 1

    option = input("Do you want to continue?? (yes/no)")


print("Number of times the die was thrown:" + str(count))
