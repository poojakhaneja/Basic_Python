
for row in range(10):
    for col in range(5):
        if (col==0 and (row >4 and row<9)  )or (col==4 and (row>0 or row<3)) or row==0 or row==4 or row==9:
            print('* ',end='')
        else:
             print(end='  ')

    print()
