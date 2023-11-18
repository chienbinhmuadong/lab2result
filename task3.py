MIN = -9
MAX = 9
red='\u001b[31m'
reset='\u001b[0m'
point1=f"{red} +{reset}" 
point2=f"{red} + {reset}"
width_graphic=10
for i in range (width_graphic): 
    if i !=MAX:
        print(f"{' . '*i}{point2}{' . '*(9-i-1)}{9-i}{' . '*(9-i-1)}{point1}{'  .'*i}")
    else:
        print(" ".join(map(str, range(MIN, 1))), '  '.join(map(str, range(1,MAX+1))))
