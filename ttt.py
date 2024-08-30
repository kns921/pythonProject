s = input()
try:
    i = int(s)
except ValueError:
    i = None

if isinstance(i, int):
    print('YES')
else:
    print('NO')
