#from solving https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(letters):
    i = 1
    newStr = ""
    for x in letters:
        for y in range(i):
            if (y == 0):
                newStr = newStr + x.upper()
            else:
                newStr = newStr + x.lower()
        newStr = newStr + "-"
        i = i + 1
    newStr = newStr[:-1]
    return newStr


str = accum("abcd")
print(str)

str = accum("RqaEzty")
print(str)

str = accum("cwAt")
print(str)





