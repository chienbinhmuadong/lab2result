yellow='\u001b[43m'
green='\u001b[42m'
red='\u001b[41m'
reset='\u001b[0m'
print('изображение флага Литвы: ')
row=6
length=20
for i in range (row):
    if i in [0,1] :
        print(f'{yellow}{" "*length}{reset}')
    elif i in [2,3] :
        print(f'{green}{" "*length}{reset}')
    else:
        print(f'{red}{" "*length}{reset}')
