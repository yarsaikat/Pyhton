# Bubble sort using python
# list = [1, 3, 4, 6, 9, 4]
# def sort(list):
#     for i in range(len(list)-1, 0, -1):
#         for j in range(i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
# sort(list)
# print(list)

# list = [1, 3, 4, 6, 9, 4]
# def sort(list):
#     for i in range(len(list)-1, 0, -1):
#         for j in range(i):
#             if list[j] > list[j + 1]:
#                 temp = list[j]
#                 list[j] = list[j + 1]
#                 list[j + 1] = temp
# sort(list)
# print(list)

# Selection sort using python
list = [1, 3, 4, 6, 9, 4]
def sort(list):
    for i in range(len(list) - 1):
        minvalue = i
        for j in range(i, len(list)):
            if list[j] < list[i]:
                minvalue = j
        list[i], list[minvalue] = list[minvalue], list[i]
sort(list)
print(list)
