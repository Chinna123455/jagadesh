## write a program to create a new list with zero's at the start and one's at the end
## l = [0, 1, 1, 1, 0, 0, 1]


l = [0, 1, 1, 1, 0, 0, 1]
l.sort()  # we performed sorting method to get 0's at the start and 1's at the end
print(l)


print("####### or #######")

# creating an empty list to store o/p
op = []

# condition to perform
for i in l:
    if i == 0:  # if i is equal to 0
        op.append(i) # insert into the empty list
    elif i == 1: # performing another condition if else i is equal to 1
        op.append(i) # insert into the list

print(op)  # to see the resultant o/p
