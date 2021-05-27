#from solving https://www.codewars.com/kata/550f22f4d758534c1100025a

def dir_reduc(directions):
    reducedDir = []
    prevDir = ""
    
    for i in directions:
        if i == "NORTH":
            if prevDir == "SOUTH":
                reducedDir.pop()
            else:
                reducedDir.append(i)
        elif i == "SOUTH":
            if prevDir == "NORTH":
                reducedDir.pop()
            else:
                reducedDir.append(i)
        elif i == "EAST":
            if prevDir == "WEST":
                reducedDir.pop()
            else:
                reducedDir.append(i)
        elif i == "WEST":
            if prevDir == "EAST":
                reducedDir.pop()
            else:
                reducedDir.append(i)
        
        if (reducedDir != []):
            prevDir = reducedDir[len(reducedDir) - 1]
        else:
            prevDir = ""
        
    return reducedDir


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

print(dir_reduc(["NORTH", "SOUTH", "EAST", "WEST"]))

print(dir_reduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))

print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]))




