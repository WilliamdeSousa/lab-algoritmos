p1 = int(input())
p2 = int(input())
p3 = int(input())
if not 0 <= p1 <= 100 or not 0 <= p2 <= 100 or not 0 <= p3 <= 100:
    print('Violacao das restricoes')
else:
    if p1 == p2 == p3:
        print('3 trofeus e 0 placa')
    elif p1 == p2 > p3 or p2 == p3 > p1 or p1 == p3 > p2:
        print('2 trofeus e 1 placa')
    elif p1 == p2 < p3 or p2 == p3 < p1 or p1 == p3 < p2:
        print('1 trofeu e 2 placas')
    else:
        print('1 trofeu e 1 placa')