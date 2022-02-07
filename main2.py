a = 'South 11 West 9 North 73'
b = a.split()

def begin_cord():
    for i in b[0::2]:
        if i == 'South' or i == 'West':
            print('0 -')
        else:
            print('0 ')

def end_cord():
    for i in b[1::2]:
        print(i)

print(begin_cord(),end_cord())


















