# persons=['Ivan', 'Anastasia', 'Nikolay', 'Daria']
#
# for f in persons:
#     # if  f == 'Anastasia':
#     #     var='Инженер ' + f
#     #     print(var)
#     print(len(f))
# print("----")
#
# a = 82 // 3**2 % 7
# print(a)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for f in num:
#     a = f ** 2
#     print(a)

# numbers = list(map(int, input().split()))
# var = 0
#
# for f in numbers:
#     var += f
# print(var)
#

# numbers = list(map(int, input().split()))
# var = 0
#
# for f in numbers:
#     if f % 2 == 0:
#         var += f
# print(var)

# films = input().split()
#
# for i, films in enumerate(films):
#     print(f"Индекс {i}: {films}")

films = input().split()
var = 0
for f in films:
    var += len(f)
print(var)
