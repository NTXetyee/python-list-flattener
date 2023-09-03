def flatten(myList):
    d = []
    for i in myList:
        if type(i) == list:
            for j in i:
                d.append(j)
        else:
            d.append(i)
    return d


x = eval(input())



listInList = True
while listInList:
    x = flatten(x)
    counter = len(x)
    for i in x:
        counter -= 1
        if type(i) == list:
            break
        else:
            if counter <= 0:
                listInList = False
                break



print(x)
