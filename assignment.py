import numpy as np


def calc(a, b, c):
    try:
        if (len(a) == 0):
            raise Exception("Null value passed")
        elif (b == "mean" ):
            print("Mean of the list: " + str(np.mean(a)))
        elif(b == "std"):
            print("Standard Deviation of the list: " + str(np.std(a)))
        else:
            raise Exception("Formula Error: Wrong Formula!")

    except Exception as e:
        print(e)


calc([1, 2, 3, 4, 5, 6, 7], "mean", 25)
