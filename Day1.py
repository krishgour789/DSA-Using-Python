# my_array = [1,2,3,5,4,5] # array of numbers
# minVal = my_array[0]     # initialize minVal to the first element of the array
# for i in my_array:       # loop through each element in the array
#     if i < minVal:       # if the current element is less than minVal, update minVal
#         minVal = i
# print(minVal)

# Find the Fibonacci series using the loop

# prev2 = 0
# prev1 = 1
# print(prev2)
# print(prev1)
# for i in range(18):
#     newfibo = prev2 + prev1
#     print(newfibo)
#     prev2= prev1
#     prev1 = newfibo


# my_array = [8,3,5,4,]
# minVal = my_array[0]
# print(minVal)

# num = int(input('enter a number :'))
# while num!=10:
#     print(num,num*num)
#     num=int(input("enter a number"))

# count= 0
# while count<10:
#     print(count,count*count,count*count*count)
#     count+=1

s = "Mumbai"
lst = ['desert','to','krish','lose']
tpl = (12,2,3,34,53)
i = 0
while i<len(lst):
    print(i,s[i],lst[i],tpl[i])
    i+=1