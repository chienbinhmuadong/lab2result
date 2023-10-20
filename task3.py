red='\u001b[31m'
reset='\u001b[0m'
point1=f"{red} +{reset}" 
point2=f"{red} + {reset}"
for i in range (10): 
    if i !=9:
        print(f"{' . '*i}{point2}{' . '*(9-i-1)}{9-i}{' . '*(9-i-1)}{point1}{'  .'*i}")
    else:
        print("-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1  2  3  4  5  6  7  8  9")
         