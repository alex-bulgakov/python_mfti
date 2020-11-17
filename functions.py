import math as mt


def foo(arr):
    result = []
    for x in arr:
        result.append(mt.log(1) + (x*x)*(1/(mt.e*mt.sin(x) + 1))/((5/4) + (1/x*5)))
    return result


def foo2(arr):
    result = []
    for x in arr:
        result.append(x*x - x - 6)
    return result


def foo3(arr):
    result = []
    for x in arr:
        result.append(mt.log10(mt.pow(1+mt.tan(1/(1+mt.pow(mt.sin(x), 2))), (x*x + 1)*mt.exp(-(abs(x)/10)))))
    return result


# def abs(x):
#     if x > 0:
#         return x
#     else:
#         return -x
