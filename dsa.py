# my_array = [3,4,64.3]
# minValu = my_array[0]
# for i  in my_array:
#     if i< minValu:
#         minValu = i
# print(minValu)


# a = [12,23,54,23,56,34,6]
# n = len(a)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)

def say_hello(name):
    return "Hello, " + name + "!"
say_hello("Alice")

# i solved this with my mind
# def square_sum(numbers):
#     n = len(numbers)
#     sum = 0
#     for i in numbers:
#         new = i**2
#         sum += new
#     return sum
