t1 = int(input())
t2 = int(input())
t3 = int(input())
t4 = int(input())
if not 2 <= t1 <= 6 or not 2 <= t2 <= 6 or not 2 <= t3 <= 6 or not 2 <= t4 <= 6:
    print('Requisito violado')
else:
    print(t1 + t2 + t3 + t4 - 3)
