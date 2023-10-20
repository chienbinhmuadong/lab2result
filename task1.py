yellow='\u001b[43m'
green='\u001b[42m'
red='\u001b[41m'
reset='\u001b[0m'
print('изображение флага Литвы: ')
for i in range (6):
    if i ==0 or i ==1 :
        print(f'{yellow}{" "*20}{reset}')
    elif i ==2 or i==3:
        print(f'{green}{" "*20}{reset}')
    else:
        print(f'{red}{" "*20}{reset}')