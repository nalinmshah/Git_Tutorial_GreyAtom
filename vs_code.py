################# new file added to test the functionality from Visual Studio code######################

l = [1, 2.3, 'New York', [6, 7]]

print ("First number is " + str(l[0]) + " last Number is "+ str(l[-1][-1]))

print (type(l[1]))

print ((l[2]).lower())

print (len(l))

print (l*2)

print(l[-1][-1])

print (l[2].replace("New","Old"))

#l = l.pop(3)

#del l[3]

print (l)

l.insert(4,"Hi")

print(l)

################# the output of the above code is as below#############
# First number is 1 last Number is 7
#<class 'float'>
#new york
#4
#[1, 2.3, 'New York', [6, 7], 1, 2.3, 'New York', [6, 7]]
#7
#Old York
#[1, 2.3, 'New York', [6, 7]]
#[1, 2.3, 'New York', [6, 7], 'Hi']
#