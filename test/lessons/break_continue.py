list = [1, 4, 8, 29, 6, 44, 56]

# for i in list:
#     # print(i)
#     if i == 6:
#         print('Ура, 6!!!')
#         break
#     print(i)

for i in list:
    if i == 56:
        print("So bad, it's 56!")
        break
    elif i == 29:
        print("Ok, it's 29!")
    elif i == 44:
        print("Great, it's 44!")
        continue
    print(i)
