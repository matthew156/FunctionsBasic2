list = [] #Question 1
def countdown(number):
     for number in range(number, -1, -1):
         if number == 0:
             return print(list)
         else:
             list.append(number)
             continue
countdown(5)

def pr(num1, num2): #Question 2
    print(num1)
    return(num2)
pr(1, 2)

def firstpluslen(arr): #Question 3
    arr = arr[0] + len(arr)
    print(arr)

firstpluslen([1,2,3,4,5,6])

#Question 4
def valuesgreaterthansecond(arr):
    variable = [] 
    variable2 = arr[1]
    for i in range(len(arr)):
        if arr[i] > variable2:
            variable.append(arr[i])
    print(len(variable))
    return variable

print(valuesgreaterthansecond([5,2,3,2,1,4]))


def thislengththatvalue(num1, num2):
    
    finalArray = []
    for i in range(0, num1):
        finalArray.append(num2)
    return finalArray
print(thislengththatvalue(5, 2))

