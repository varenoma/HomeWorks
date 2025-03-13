from math import *


def geometrigini(numbers):
    res = pow(prod(numbers),1/len(numbers))
    return res

def arifmetigi(numbers):
    res = sum(numbers) / len(numbers)
    return res


a,b = map(int, input().split())

if geometrigini([a,b]) > arifmetigi([a,b]):
    print("<")

elif geometrigini([a,b]) < arifmetigi([a,b]):
    print(">")

else:
    print("=")