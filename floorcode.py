# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
currentfloor = 6
list_of_floor = [8,9,7,10]
listnew=[]
for floor in list_of_floor:
    #print(floor)
    if currentfloor <= floor:
        #print(floor)
        listnew.append(floor)
listnew.sort()
print(listnew)

